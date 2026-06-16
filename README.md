# DeceptAI

## AI-Powered Dark Pattern Auditor

DeceptAI is an AI-powered Regulatory Technology (RegTech) platform that automatically detects deceptive UI/UX dark patterns from screenshots, advertisements, landing pages, and digital interfaces.

The platform uses OCR-based text extraction, rule-based dark pattern detection, risk scoring, confidence analysis, dashboard analytics, and PDF report generation to help identify manipulative design practices and improve digital transparency.

---

## Features

### OCR-Based Text Extraction

Extracts visible text from uploaded screenshots and interface captures using OCR.

### Dark Pattern Detection

Detects deceptive patterns such as:

* Scarcity ("Only 2 left")
* Urgency ("Limited offer")
* Pressure ("Act now")
* Social Proof ("Trusted by thousands")
* Subscription Traps
* Confirmshaming

### Risk Scoring Engine

Calculates a deception score and classifies evidence into:

* Low Risk
* Medium Risk
* High Risk

### Confidence Scoring

Generates confidence percentages indicating detection reliability.

### Dashboard Analytics

Provides:

* Total audits
* Average confidence score
* Highest detected score
* Risk distribution
* Dark pattern distribution
* Audit history

### Violations Management

Displays medium-risk and high-risk findings for investigation and review.

### PDF Report Export

Generates downloadable audit reports containing:

* Risk assessment summary
* Confidence score
* Pattern explanations
* OCR extracted evidence

### Evidence Storage

Stores uploaded screenshots and audit records using Supabase Database and Storage.

---

## System Workflow

```text
Upload Evidence
        ↓
OCR Text Extraction
        ↓
Dark Pattern Detection
        ↓
Deception Score Calculation
        ↓
Confidence Assessment
        ↓
Risk Classification
        ↓
Store Audit Record
        ↓
Dashboard Analytics
        ↓
Violations Review
        ↓
PDF Report Export
```

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* Shadcn UI

### Backend

* FastAPI
* Python

### Database & Storage

* Supabase Database
* Supabase Storage

### OCR & Detection

* EasyOCR
* OpenCV
* Rule-Based Detection Engine

---

## Project Structure

```text
frontend/
├── app/
│   ├── dashboard/
│   ├── upload/
│   └── violations/
├── components/
├── lib/

backend/
├── services/
│   ├── ocr_service.py
│   └── detection_service.py
├── main.py
```

---

## Current Capabilities

* Screenshot analysis
* OCR text extraction
* Dark pattern detection
* Risk scoring
* Confidence scoring
* Audit storage
* Dashboard analytics
* Violations tracking
* PDF report generation

---

# Screenshots

## Dashboard

Features:

* Audit statistics overview
* Average confidence tracking
* Risk distribution chart
* Dark pattern distribution chart
* Evidence audit cards

<img width="945" height="441" alt="Dashboard" src="https://github.com/user-attachments/assets/2dd439ef-1b39-4412-b32d-1f4d1712a5fa" />

---

## Upload Evidence

Features:

* Screenshot upload
* OCR extraction
* Dark pattern analysis
* Risk scoring

<img width="949" height="180" alt="Upload Evidence" src="https://github.com/user-attachments/assets/fdc838ab-33d1-45f7-9cd9-3ebcc65ae11e" />

---

## Violations Page

Features:

* Medium-risk findings
* High-risk findings
* Evidence review interface
* OCR evidence display

<img width="949" height="442" alt="Violations Page" src="https://github.com/user-attachments/assets/6af6af60-277a-49fe-8ae4-415bfa19dea7" />

---

## Audit Detail View

Features:

* OCR evidence inspection
* Confidence scoring
* Risk classification
* Pattern review
* Report export functionality

<img width="961" height="1637" alt="image" src="https://github.com/user-attachments/assets/eb43154c-a6a9-4467-9a68-723e50809dfb" />





---

## PDF Export Report

Features:

* Automated report generation
* Risk assessment summary
* Confidence scoring
* Pattern explanations
* OCR evidence summary

<img width="934" height="832" alt="image" src="https://github.com/user-attachments/assets/6f97c8e0-70cc-4ad1-85ae-5f6eb0f89c4a" />



---

## Example Detection

### Input Text

```text
ONLY 2 LEFT

LIMITED OFFER

ACT NOW
```

### Detection Output

```text
Score: 70
Risk: High

Patterns Detected:
- Scarcity
- Urgency
```

---

## Motivation

Dark patterns are deceptive user interface techniques designed to manipulate user behavior and influence user decisions.

DeceptAI aims to provide an automated auditing platform capable of identifying such practices from screenshots, advertisements, and digital interfaces. The goal is to improve transparency, user trust, and ethical design practices through AI-assisted compliance analysis.

---

## Future Improvements

* Machine learning based detection
* Advanced scoring algorithms
* Pattern explanation engine
* User authentication
* Cloud deployment
* Real-time monitoring
* Compliance benchmarking
* Browser extension integration

---

## Project Status

### DeceptAI v1.0

Completed Features:

* OCR text extraction
* Dark pattern detection
* Risk scoring
* Confidence scoring
* Dashboard analytics
* Violations management
* PDF export reports
* Supabase integration

---

## Author

**Srijan Akshit**

Developed as an AI-powered dark pattern auditing platform for detecting deceptive UX practices and improving digital transparency.
