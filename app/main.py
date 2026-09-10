# from fastapi import FastAPI
# from pydantic import BaseModel

# from app.rag import get_answer

# app = FastAPI()


# class ChatRequest(BaseModel):
#     question: str


# @app.get("/")
# def home():
#     return {
#         "project": "AI Banking RAG Assistant",
#         "status": "Running Successfully"
#     }


# @app.post("/chat")
# def chat(request: ChatRequest):

#     answer = get_answer(request.question)

#     return {
#         "question": request.question,
#         "answer": answer
#     }

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body
from fastapi import Form

# from app.ingest import get_answer
from app.rag import get_answer
app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Banking Assistant is Running Successfully"}




# QUESTION WITH STRING BODY

# @app.post("/chat")
# def chat(request: Question):

#     answer = get_answer(request.question)

#     return {
#         "question": request.question,
#         "answer": answer
#     }



# QUESTION WITH BODY PARAMETER

# @app.post("/chat")
# def chat(question: str = Body(...)):
#     answer = get_answer(question)
#     return {"answer": answer}

# QUESTION WITH FORM PARAMETER

@app.post("/chat")
def chat(question: str = Form(...)):
    answer = get_answer(question)
    return {"answer": answer}