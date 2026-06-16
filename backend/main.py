from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.ocr_service import extract_text
from services.detection_service import analyze_text
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Dark Pattern Auditor Backend Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text(temp_path)
    print("OCR TEXT:", extracted_text)

    os.remove(temp_path)

    result = analyze_text(extracted_text)

    return {
    "filename": file.filename,
    "extracted_text": extracted_text,

    "deception_score": result["score"],
    "risk_level": result["risk"],

    "patterns": result["patterns"],
    "matches": result["matches"],

    "explanations": result["explanations"],

    "confidence": result["confidence"],

    "trust_score": result["trust_score"],
    "compliance_grade": result["compliance_grade"],

    "audit_summary": result["audit_summary"],

    "highlights": result["highlights"],

    "recommendations": result["recommendations"],

    "regulations": result["regulations"],

    "severity": result["severity"]
}