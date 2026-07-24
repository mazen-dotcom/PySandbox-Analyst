# PySandbox-Analyst (Sandboxed Code Interpreter)

An interactive, web-based data analysis workbench that converts natural language prompts and uploaded datasets into executable Python code. Code is executed safely inside an isolated Docker sandbox, returning live terminal logs, interactive charts, and structured data insights.

---

## 🌟 Key Features

- 📊 **Interactive Data Workbench:** Upload CSVs/JSON files and query them using natural language.
- 🔒 **Secure Docker Sandbox:** Isolated, network-disabled execution environment preventing host OS access or network leaks.
- 📈 **Dynamic Interactive Charts:** Seamlessly renders interactive visualizations (Chart.js / Plotly / Recharts) instead of static image files.
- 🔄 **Self-Healing Code Loop:** Automatically catches Python execution errors (`stderr`), feeds logs back to the AI, and patches code in real time until successful.
- ⚡ **Live Execution Stream:** Streams `stdout` and `stderr` logs to the frontend via WebSockets/SSE.

---


