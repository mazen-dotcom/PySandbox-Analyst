import os
import agentSandbox
from google import genai
from google.genai import types
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. Configuration & Section Map Definition
# ---------------------------------------------------------------------------
DOCS_FILE_PATH = "plotly-docs.md"

SECTION_MAP = {
    "Overview and Introduction": {"start": 1, "end": 8},
    "Top-Level Object Structure": {"start": 9, "end": 28},
    "Trace Types Overview": {"start": 29, "end": 32},
    "Cartesian and 2D Coordinate Traces": {"start": 33, "end": 343},
    "Polar and Radial Coordinate Traces": {"start": 344, "end": 380},
    "Circular and Sector-Based Traces": {"start": 381, "end": 446},
    "Hierarchical and Tree-Based Traces": {"start": 447, "end": 520},
    "Statistical and Distribution Traces": {"start": 521, "end": 601},
    "Financial and Time-Series Traces": {"start": 602, "end": 699},
    "Flow and Relationship Diagram Traces": {"start": 700, "end": 742},
    "Geographic and Map-Based Traces": {"start": 743, "end": 839},
    "Three-Dimensional and Volume Traces": {"start": 840, "end": 1045},
    "Table and Indicator Traces": {"start": 1046, "end": 1136},
    "WebGL-Accelerated Scatter Traces": {"start": 1137, "end": 1182},
    "Layout and Visual Styling": {"start": 1183, "end": 1880},
    "Configuration and Behavior Settings": {"start": 1881, "end": 1960},
    "Animation and Frame Sequences": {"start": 1961, "end": 2008},
    "Usage Examples and Code Samples": {"start": 2009, "end": 2115},
    "Reference Links and External Resources": {"start": 2116, "end": 2131},
}

# ---------------------------------------------------------------------------
# 2. Define Custom Documentation Fetcher Tool
# ---------------------------------------------------------------------------
def fetch_doc_section(section_title: str) -> str:
    """Reads specific line ranges from the documentation based on section title.

    Args:
        section_title: The exact title of the section to load. Must be one of:
            - 'Overview and Introduction'
            - 'Top-Level Object Structure'
            - 'Trace Types Overview'
            - 'Cartesian and 2D Coordinate Traces'
            - 'Polar and Radial Coordinate Traces'
            - 'Circular and Sector-Based Traces'
            - 'Hierarchical and Tree-Based Traces'
            - 'Statistical and Distribution Traces'
            - 'Financial and Time-Series Traces'
            - 'Flow and Relationship Diagram Traces'
            - 'Geographic and Map-Based Traces'
            - 'Three-Dimensional and Volume Traces'
            - 'Table and Indicator Traces'
            - 'WebGL-Accelerated Scatter Traces'
            - 'Layout and Visual Styling'
            - 'Configuration and Behavior Settings'
            - 'Animation and Frame Sequences'
            - 'Usage Examples and Code Samples'
            - 'Reference Links and External Resources'
    """
    if section_title not in SECTION_MAP:
        return f"Error: Section '{section_title}' does not exist. Choose from: {list(SECTION_MAP.keys())}"

    start_line = SECTION_MAP[section_title]["start"]
    end_line = SECTION_MAP[section_title]["end"]

    try:
        if not os.path.exists(DOCS_FILE_PATH):
            return f"Error: Documentation file '{DOCS_FILE_PATH}' was not found on disk."

        with open(DOCS_FILE_PATH, "r", encoding="utf-8") as file:
            # File line indices are 1-based as specified in SECTION_MAP
            lines = file.readlines()
            # Python slice is 0-indexed, so start_line - 1 to end_line
            selected_lines = lines[start_line - 1 : end_line]
            return "".join(selected_lines)

    except Exception as e:
        return f"Error reading documentation file: {str(e)}"
########################################
def run_python(code: str) -> str:
    """Runs Python code and returns the output.

    Args:
        code: The Python source code to execute.
    """
    return agentSandbox.execute_code(code)



# ---------------------------------------------------------------------------
# 3. Main Execution Workflow
# ---------------------------------------------------------------------------
def run_assistant():
    client = genai.Client()
    #userdataset = open("train.csv", 'r')
    #parent_dir = Path.cwd().parent
    #print(parent_dir)
    #uploaded_file = client.files.upload(file=f"testdata/train.csv")
    agentSandbox.upload_files_to_sandbox(['testdata/train.csv'])
    
    f = open("sys_prompt_dash_v3.md", 'r')
    lst = f.readlines()
    lst = "".join(lst)
    #print(lst)
    f.close()
    system_instruction = lst
    
    # Pass BOTH tools: your custom doc tool AND the Google code execution sandbox tool
    tools_list = [
        fetch_doc_section,
         run_python,
        #types.Tool(code_execution=types.ToolCodeExecution())
        
    ]
    #tool_config = types.ToolConfig(
        #include_server_side_tool_invocations=True
    #)

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=tools_list,
        thinking_config=types.ThinkingConfig(include_thoughts=True)

        #tool_config=tool_config
    )

    user_query = (
        "give me general insights about this data."
    )

    print(f"User Question: {user_query}\n")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[user_query],
        #config=types.GenerateContentConfig(
        #    system_instruction=system_instruction,
        #    tools=tools_list,    
        #)
        config=config
    )

    # Output response
    print("=== FINAL ASSISTANT RESPONSE ===")
    print(response.text)

    # Inspect Sandbox Executions if code was executed
    print("\n=== EXECUTION AUDIT TRAIL ===")
    for candidate in response.candidates:
        for part in candidate.content.parts:
            if part.executable_code:
                print("\n[Generated Python Code]:")
                print(part.executable_code.code)
            if part.code_execution_result:
                print("\n[Sandbox Output]:")
                print(part.code_execution_result.output)

            if part.thought:
                print("Thought Process:")
                print(part.text)
                

if __name__ == "__main__":
    run_assistant()