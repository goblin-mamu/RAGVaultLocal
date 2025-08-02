🧠 Local LLM with RAG & Web UI
Welcome to Local LLM with RAG—a sleek, offline AI assistant that runs directly on your Windows PC! Just upload your PDFs or text files, ask questions, and get smart, context-aware answers powered by a local language model with Retrieval-Augmented Generation (RAG).

No cloud. No tracking. Just you, your data, and your local AI.

🌟 Features
Local LLM: Runs phi-3 (3.8B params) via Ollama—lightweight and fast.

RAG Magic: Context-aware querying using your own docs stored in C:\MyLLM\data.

Web UI: Simple Flask-based interface at http://localhost:5000.

Offline: Fully functional after setup—no internet required.

Performance Optimized: Fast startup, indexed context, and limited prompt size for speed.

🛠 System Architecture
📌 Overview
A self-contained RAG app for Windows 10/11, blending Python, Rust, and a clean browser-based frontend.

⚙️ Components
Layer	Technology
🧠 Model	phi-3 via Ollama
🔍 Embeddings	all-MiniLM-L6-v2 via sentence-transformers
🗃️ Vector DB	ChromaDB
🌐 Web UI	Flask
📄 PDF Parsing	PyPDF2
🦀 Tokenizers	Rust + PyO3
🐍 Scripting	PowerShell for setup
💾 Storage	Local directory: C:\MyLLM\data

📂 File Structure
makefile
Copy
Edit
C:\MyLLM
├── app.py            # Flask app with RAG logic and UI
├── data/             # Upload .txt/.pdf files here
├── chroma_db/        # Vector DB for embeddings
├── setup_log.txt     # Setup logs
└── README.txt        # Usage guide
🔁 Data Flow
mermaid
Copy
Edit
graph LR
A[User] --> B[Browser: localhost:5000]
B --> C[Flask: app.py]
C --> D[Upload to C:\MyLLM\data]
C --> E[Query Input]
E --> F[Sentence Transformers]
F --> G[Rust Tokenizers]
F --> H[ChromaDB]
H --> I[Ollama: phi-3]
I --> J[Response]
J --> B
⚙️ Setup Instructions
✅ Prerequisites
Windows 10/11

Internet (for initial setup)

📥 Installation Steps
Install Python 3.12.7

Download

During install: ✅ "Add Python to PATH"

Verify: python --version → 3.12.7

Install Rust

Download rustup

Run rustup-init.exe, accept defaults

Verify: rustc --version → e.g., 1.81.0

Clone and Run Setup

powershell
Copy
Edit
git clone <your-repo-url>
cd .\Local-LLM-RAG\
powershell .\setup_llm.ps1
Choose: C:\MyLLM as install path (or custom)

Pick setup mode: 1 (Internet Mode)

Launch the App

powershell
Copy
Edit
python C:\MyLLM\app.py
Use the Web UI

Visit: http://localhost:5000

Upload .txt or .pdf files

Ask questions (e.g., “Summarize this”)

⚡ Performance
Indexing: ~30 seconds at startup or after uploads.

Query Response: ~2–10 seconds (CPU-based).

Optimizations:

Reduced prompt context: 1000 characters

Fast embeddings: MiniLM

Local inference: phi-3 (can be swapped)

Want more speed?

bash
Copy
Edit
ollama pull gemma:2b
🧪 Tech Notes
Python 3.13 Issue: Incompatible with PyO3 tokenizer bindings—stuck to 3.12.

Rust Needed: For tokenizers in transformers.

Model Tuning: Switched from LLaMA 3 (slow, 7B) to Phi-3 (faster, 3.8B).

RAG Optimization: Indexing moved from runtime to startup/upload.

🚀 How to Share
Create a GitHub Repo:

Name it something like local-llm-rag

Add a short description and initialize with a README

Upload Files:

README.md (this file)

app.py and setup_llm.ps1

Push It:

bash
Copy
Edit
git add .
git commit -m "Initial commit: local LLM with RAG"
git push origin main
Share Your Repo URL with friends or teams.

🙌 Credits
Made with 💻 by Bhavya  & Grok 3 (xAI) – April 2025

Have questions or ideas? Drop them in the [Issues]
