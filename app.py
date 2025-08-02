from flask import Flask, request, render_template_string
import ollama
import chromadb
from sentence_transformers import SentenceTransformer
import os
import PyPDF2
import time

app = Flask(__name__)
client = chromadb.PersistentClient(path=r"C:\MyLLM\chroma_db")
collection = client.get_or_create_collection("rag_collection")
model = SentenceTransformer('all-MiniLM-L6-v2')
data_folder = r"C:\MyLLM\data"

# Ensure data folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

def index_documents():
    """Index all files in data_folder into ChromaDB."""
    start_time = time.time()
    # Clear old data to avoid duplicates (optional: comment out if you want to append)
    collection.delete(ids=collection.get()['ids'])
    for filename in os.listdir(data_folder):
        filepath = os.path.join(data_folder, filename)
        if filename.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
        elif filename.endswith('.pdf'):
            with open(filepath, 'rb') as f:
                pdf = PyPDF2.PdfReader(f)
                text = " ".join(page.extract_text() for page in pdf.pages)
        else:
            continue
        embedding = model.encode(text).tolist()
        collection.add(ids=[filename], embeddings=[embedding], documents=[text])
    print(f"Indexing completed in {time.time() - start_time:.2f} seconds.")

# Index at startup
print("Indexing documents at startup...")
index_documents()
print("Startup indexing complete.")

@app.route('/', methods=['GET', 'POST'])
def chat():
    response = ""
    start_time = time.time()
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename:
                filepath = os.path.join(data_folder, file.filename)
                file.save(filepath)
                print(f"Uploaded {file.filename}. Re-indexing...")
                index_documents()
                response = f"Uploaded {file.filename} successfully."
        elif 'query' in request.form:
            query = request.form['query']
            # Query ChromaDB (fast, since indexing is done)
            results = collection.query(query_texts=[query], n_results=3)
            context = " ".join(doc for doc in results['documents'][0] if doc)
            prompt = f"Context: {context}\nQuery: {query}"
            # Generate response with Ollama
            response = ollama.generate(model='llama3', prompt=prompt)['response']
    elapsed_time = time.time() - start_time
    return render_template_string('''
        <h1>Local LLM Chat</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
        <form method="post">
            <input type="text" name="query" placeholder="Ask something..." style="width: 300px;">
            <input type="submit" value="Send">
        </form>
        <p>{{ response }}</p>
        <p>Response time: {{ elapsed_time }} seconds</p>
    ''', response=response, elapsed_time=f"{elapsed_time:.2f}")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)