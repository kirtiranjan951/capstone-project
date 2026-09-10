from pathlib import Path
import chromadb
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# -------------------------------
# Text Splitter
# -------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

# -------------------------------
# Embedding Model
# -------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------
# ChromaDB
# -------------------------------
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="bank_policy"
)

# -------------------------------
# Read all PDFs
# -------------------------------
pdf_folder = Path("documents")

for pdf_file in pdf_folder.glob("*.pdf"):

    print(f"\nProcessing: {pdf_file.name}")

    # Check whether this PDF is already indexed
    existing = collection.get(
        where={"source": pdf_file.name}
    )

    if len(existing["ids"]) > 0:
        print(f"{pdf_file.name} already indexed. Skipping...")
        continue

    # Read PDF
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    # Split into chunks
    chunks = text_splitter.split_text(text)

    print(f"Chunks : {len(chunks)}")

    # Create embeddings
    embeddings = model.encode(chunks)

    # Store chunks
    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[f"{pdf_file.stem}_{i}"],
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            metadatas=[
                {
                    "source": pdf_file.name
                }
            ]
        )

    print(f"{pdf_file.name} indexed successfully.")

print("\nAll documents processed.")

print("Total Records :", collection.count())





# result = collection.get(limit=5)

# print(result["metadatas"])