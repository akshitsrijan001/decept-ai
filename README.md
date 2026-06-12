 # DeceptAI

DeceptAI is an AI-powered dark pattern auditing platform that helps identify deceptive UI and marketing practices from screenshots and digital evidence.

Users can upload screenshots, advertisements, landing pages, or interface captures. The system extracts text using OCR, detects dark pattern indicators, assigns a deception score, classifies risk levels, and stores audit records for review.

## Features

### OCR-Based Text Extraction

Extracts visible text from uploaded screenshots and UI captures.

### Dark Pattern Detection

Identifies common deceptive patterns such as:

* Scarcity ("Only 2 left")
* Urgency ("Limited offer")
* Pressure ("Act now")

### Risk Scoring Engine

Generates a deception score and classifies evidence as:

* Low Risk
* Medium Risk
* High Risk

### Audit Dashboard

Provides:

* Total audits
* Risk distribution statistics
* Visual analytics
* Evidence history

### Violations Management

Displays medium-risk and high-risk findings for easier investigation.

### Evidence Storage

Stores uploaded evidence and audit records using Supabase.

---

## System Workflow

Upload Evidence

↓

OCR Text Extraction

↓

Dark Pattern Detection

↓

Deception Score Calculation

↓

Risk Classification

↓

Store Audit Record

↓

Dashboard & Violations Review

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### Database & Storage

* Supabase Database
* Supabase Storage

### OCR & Detection

* OCR Processing
* Rule-Based Dark Pattern Detection Engine

---

## Project Structure

frontend/
├── app/
│ ├── dashboard/
│ ├── upload/
│ └── violations/
├── components/
├── lib/

backend/
├── services/
│ ├── ocr_service.py
│ └── detection_service.py
├── main.py

---

## Current Capabilities

* Screenshot analysis
* OCR text extraction
* Dark pattern keyword detection
* Risk scoring
* Audit storage
* Dashboard analytics
* Violations tracking

---

## Future Improvements

* Advanced scoring algorithms
* Machine learning based detection
* Pattern explanations
* PDF audit reports
* Authentication and user accounts
* Cloud deployment
* Real-time monitoring

---

## Author

**Srijan Akshit**

Developed as an AI-assisted dark pattern auditing platform for detecting deceptive UX practices and improving digital transparency.
