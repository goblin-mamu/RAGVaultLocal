# Directory: .

/filename.pdf: [non-readable or binary content]
/README.txt: 
```
﻿Local LLM Setup README
=====================
Setup completed on 04/06/2025 15:28:24

Usage:
1. Place text files and PDFs in C:\MyLLM\data for RAG.
2. Run the web UI with: python "C:\MyLLM\app.py"
3. Open a browser and go to http://localhost:5000
4. Type your query and press Send.

Debugging:
- Check C:\MyLLM\setup_log.txt for logs.
- Ensure Ollama is running (start it manually if needed).

Air-gapped Mode:
- Pre-download OllamaSetup.exe and .whl files to C:\MyLLM\deps.
- Model files should be in Ollama's default storage (e.g., C:\Users\YourUser\.ollama).

Security:
- Runs on localhost only (127.0.0.1).
- No external connections after setup in air-gapped mode.

```
