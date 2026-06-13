<<<<<<< HEAD
# AI-Driven Dark Pattern Auditor

An AI-powered Regulatory Technology (RegTech) platform that automatically detects deceptive UI/UX dark patterns from screenshots and user flows.
=======
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
>>>>>>> f32eae677342698a19a023e4f7319c29f4cec20e

## Tech Stack

### Frontend
<<<<<<< HEAD
- Next.js
- React
- Tailwind CSS
- Shadcn UI

### Backend
- FastAPI

### AI Stack
- PyTorch
- OpenCV
- EasyOCR
- Transformers

### Database
- Supabase

## Planned Features

- Screenshot Upload
- OCR Extraction
- Dark Pattern Detection
- Compliance Reports
- Risk Scoring
- Annotated Screenshots

## Project Status

Day 1 Completed
=======

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

## Screenshots

### Dashboard

* Audit statistics overview
* Risk distribution chart
* Evidence audit cards

### Upload Evidence

* Screenshot upload
* OCR extraction
* Dark pattern analysis
* Risk scoring

### Violations Page

* Medium-risk findings
* High-risk findings
* Evidence review interface

---

## Example Detection

Input Text:

ONLY 2 LEFT

LIMITED OFFER

ACT NOW

Detection Output:

Score: 70

Risk: High

Patterns Detected:

* Scarcity
* Urgency

---

## Motivation

Dark patterns are deceptive user interface techniques designed to manipulate user behavior. DeceptAI aims to provide an automated auditing system capable of identifying such practices from screenshots, advertisements, and digital interfaces.

The goal is to help improve transparency, user trust, and ethical design practices.


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
>>>>>>> f32eae677342698a19a023e4f7319c29f4cec20e
