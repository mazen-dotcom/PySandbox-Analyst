import json
from abc import ABC, abstractmethod
from typing import List, Callable, Dict, Any

from openai import OpenAI
from google import genai
from google.genai import types


class ProviderStrategy(ABC):
    def __init__(self):
        self.tools_schema: list = []
        self.available_tools: Dict[str, Callable] = {}
        self.system_prompt: str = ""
        self.chat_history: list = []

    def setToolsSchema(self, toolsDict: list):
        """Expects a tools list dictionary in the OpenAI API format."""
        self.tools_schema = toolsDict

    def setAvailableTools(self, toolsList: List[Callable]):
        """Takes a list of actual functions and maps them by __name__."""
        self.available_tools = {func.__name__: func for func in toolsList}

    def setSystemPrompt(self, prompt: str):
        """Expects a System prompt as a string."""
        self.system_prompt = prompt

    @abstractmethod
    def getChatResponse(self, userPrompt: str) -> str:
        pass

    @abstractmethod
    def loadChatHistory(self, historyList: list):
        pass



class OpenAIStrategy(ProviderStrategy):
    def __init__(self, client: OpenAI = None, model: str = "gpt-4o"):
        super().__init__()
        self.client = client or OpenAI()
        self.model = model

    def loadChatHistory(self, historyList: list):
        """Loads OpenAI-formatted messages list directly into instance state."""
        self.chat_history = list(historyList)

    def _ensure_history_initialized(self, userPrompt: str):
        """Initializes chat history with system prompt if empty, then appends user prompt."""
        if not self.chat_history:
            if self.system_prompt:
                self.chat_history.append({"role": "system", "content": self.system_prompt})
        
        self.chat_history.append({"role": "user", "content": userPrompt})

    def getChatResponse(self, userPrompt: str) -> str:
        self._ensure_history_initialized(userPrompt)

        kwargs: Dict[str, Any] = {
            "model": self.model,
            "messages": self.chat_history
        }
        if self.tools_schema:
            kwargs["tools"] = self.tools_schema

      
        while True:
            response = self.client.chat.completions.create(**kwargs)
            message = response.choices[0].message
            
            
            msg_dict = message.model_dump(exclude_none=True)
            self.chat_history.append(msg_dict)

          
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    fn_name = tool_call.function.name
                    fn_args = json.loads(tool_call.function.arguments or "{}")

                
                    if fn_name in self.available_tools:
                        tool_result = self.available_tools[fn_name](**fn_args)
                    else:
                        tool_result = f"Error: Tool '{fn_name}' not found."

                   
                    content_str = (
                        tool_result if isinstance(tool_result, str) 
                        else json.dumps(tool_result)
                    )

                   
                    self.chat_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": fn_name,
                        "content": content_str
                    })
            else:
                # No tool calls requested; loop terminates
                return message.content or ""



class GeminiStrategy(ProviderStrategy):
    def __init__(self, client: genai.Client = None, model: str = "gemini-2.5-flash"):
        super().__init__()
        self.client = client or genai.Client()
        self.model = model

    def loadChatHistory(self, historyList: list):
        """
        Converts OpenAI-style JSON history list into Gemini types.Content objects.
        OpenAI roles: system, user, assistant, tool
        Gemini roles: user, model
        """
        gemini_history = []
        
        for msg in historyList:
            role = msg.get("role")
            content = msg.get("content", "")

            if role == "system":
                # System prompt is passed to Config for gemini, skip storing in history turns
                continue
            elif role == "user":
                gemini_history.append(
                    types.Content(
                        role="user", 
                        parts=[types.Part.from_text(text=content)]
                    )
                )
            elif role == "assistant":
                gemini_history.append(
                    types.Content(
                        role="model", 
                        parts=[types.Part.from_text(text=content or "")]
                    )
                )
            elif role == "tool":
                # Translate OpenAI tool output to Gemini FunctionResponse
                fn_name = msg.get("name", "unknown")
                raw_out = content
                
                try:
                    out_dict = json.loads(raw_out) if isinstance(raw_out, str) else raw_out
                except Exception:
                    out_dict = {"result": raw_out}

                if not isinstance(out_dict, dict):
                    out_dict = {"result": out_dict}

                gemini_history.append(
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_function_response(
                                name=fn_name,
                                response=out_dict
                            )
                        ]
                    )
                )

        self.chat_history = gemini_history

    def getChatResponse(self, userPrompt: str) -> str:
       
        tool_functions = list(self.available_tools.values()) if self.available_tools else None

        config = types.GenerateContentConfig(
            system_instruction=self.system_prompt if self.system_prompt else None,
            tools=tool_functions
        )

      
        chat = self.client.chats.create(
            model=self.model,
            history=self.chat_history if self.chat_history else None,
            config=config
        )

        response = chat.send_message(userPrompt)
        
        
        self.chat_history = chat.get_history()
        
        return response.text