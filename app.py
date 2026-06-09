from fastapi import FastAPI, UploadFile
from resume_parser import extract_text
from interview_generator import generate_questions

app = FastAPI()

@app.get("/")
def home():
    return {"message":"AI Resume Analyzer API"}

@app.post("/analyze")
async def analyze_resume(file: UploadFile):
    text = extract_text(await file.read())
    questions = generate_questions(text)
    return {"resume_length": len(text), "interview_questions": questions}
