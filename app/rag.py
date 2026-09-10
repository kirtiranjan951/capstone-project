import chromadb
import ollama
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("bank_policy")

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_answer(question: str):

    # Convert question to embedding
    query_embedding = model.encode(question).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )
    print("\n========== FULL QUERY RESULT ==========")
    print(results)
    print("=======================================")

    # ----------------------------
    # Print retrieved sources
    # ----------------------------
    print("\n========== Retrieved Sources ==========")

    for metadata in results["metadatas"][0]:
        print(metadata["source"])

    # ----------------------------
    # Print retrieved chunks
    # ----------------------------
    print("\n========== Retrieved Chunks ==========")

    for doc in results["documents"][0]:
        print(doc)
        print("-" * 50)

    # Create context
    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are an AI Banking Assistant.

Answer only using the context below.

If the answer is not available in the context, reply:
"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    question = input("\nEnter your question: ")
    answer = get_answer(question)

    print("\n========== FINAL ANSWER ==========")
    print(answer)