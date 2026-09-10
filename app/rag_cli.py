# import os
# import glob
# import pickle
# import argparse
# from typing import List

# import openai
# import numpy as np
# from tqdm import tqdm


# INDEX_PATH = os.path.join(os.path.dirname(__file__), "index.pkl")


# def read_documents(paths: List[str]) -> List[str]:
#     texts = []
#     for p in paths:
#         for fp in glob.glob(os.path.join(p, "**", "*.txt"), recursive=True):
#             try:
#                 with open(fp, "r", encoding="utf-8") as f:
#                     texts.append(f.read())
#             except Exception:
#                 continue
#     return texts


# def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
#     chunks = []
#     start = 0
#     length = len(text)
#     while start < length:
#         end = min(start + chunk_size, length)
#         chunks.append(text[start:end])
#         start = end - overlap
#         if start < 0:
#             start = 0
#     return chunks


# def embed_texts(texts: List[str], batch_size: int = 16) -> np.ndarray:
#     embeddings = []
#     for i in range(0, len(texts), batch_size):
#         batch = texts[i : i + batch_size]
#         resp = openai.Embedding.create(model="text-embedding-3-small", input=batch)
#         for item in resp["data"]:
#             embeddings.append(item["embedding"])
#     return np.array(embeddings, dtype=np.float32)


# def build_index(paths: List[str]):
#     docs = read_documents(paths)
#     chunks = []
#     for d in docs:
#         chunks.extend(chunk_text(d))

#     if not chunks:
#         print("No text files found under the provided paths.")
#         return

#     print(f"Generating embeddings for {len(chunks)} chunks...")
#     embeddings = embed_texts(chunks)

#     index = {"texts": chunks, "embeddings": embeddings}
#     with open(INDEX_PATH, "wb") as f:
#         pickle.dump(index, f)
#     print(f"Index saved to {INDEX_PATH}")


# def cosine_similarity(a: np.ndarray, b: np.ndarray) -> np.ndarray:
#     # a: (n, d) b: (m, d) -> (n, m)
#     a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
#     b_norm = b / np.linalg.norm(b, axis=1, keepdims=True)
#     return np.dot(a_norm, b_norm.T)


# def ask_question(query: str, top_k: int = 3):
#     if not os.path.exists(INDEX_PATH):
#         print("Index not found. Run the build command first.")
#         return

#     with open(INDEX_PATH, "rb") as f:
#         index = pickle.load(f)

#     q_emb = embed_texts([query])
#     sims = cosine_similarity(index["embeddings"], q_emb).squeeze()
#     top_idx = np.argsort(-sims)[:top_k]

#     context = "\n\n".join(index["texts"][i] for i in top_idx)

#     messages = [
#         {"role": "system", "content": "You are a helpful assistant answering questions using the provided context."},
#         {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
#     ]

#     resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=500)
#     answer = resp["choices"][0]["message"]["content"].strip()
#     print("\nAnswer:\n", answer)


# def main():
#     parser = argparse.ArgumentParser(description="Simple RAG CLI for bank assistant")
#     sub = parser.add_subparsers(dest="cmd")

#     build = sub.add_parser("build", help="Build embeddings index from text files")
#     build.add_argument("paths", nargs="*", default=["../documents", "../docs", "../reports"], help="Folders to read text files from")

#     ask = sub.add_parser("ask", help="Ask a question using the built index")
#     ask.add_argument("query", nargs="+", help="Question to ask")
#     ask.add_argument("--k", type=int, default=3, help="Number of retrieved chunks to use")

#     args = parser.parse_args()

#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         print("Please set the OPENAI_API_KEY environment variable.")
#         return
#     openai.api_key = api_key

#     if args.cmd == "build":
#         abs_paths = [os.path.abspath(os.path.join(os.path.dirname(__file__), p)) for p in args.paths]
#         build_index(abs_paths)
#     elif args.cmd == "ask":
#         query = " ".join(args.query)
#         ask_question(query, top_k=args.k)
#     else:
#         parser.print_help()


# if __name__ == "__main__":
#     main()
open("LeavePolicy.pdf")
