from pathlib import Path

DOCUMENT_PATH = Path("documents/delete_LeavePolicy.txt")


def get_answer(question: str):

    # Read document
    # with open(DOCUMENT_PATH, "rb") as file:
    with open(DOCUMENT_PATH, "r", encoding="utf-8") as file:
        policy = file.read()

    question = question.lower()

    # Search inside document
    if "annual leave" in question:
        for line in policy.splitlines():
            if "20 annual leaves" in line.lower():
                return line

    elif "medical leave" in question:
        for line in policy.splitlines():
            if "12 medical" in line.lower():
                return line

    elif "casual leave" in question:
        for line in policy.splitlines():
            if "8 casual" in line.lower():
                return line

    return "I couldn't find this information in the available policy."