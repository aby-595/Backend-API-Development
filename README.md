# Sarva Suvidhaen Backend Assignment – KPA ERP Integration

This repository contains a complete **FastAPI** backend implementation with integration to a **Flutter** frontend for handling:
- ✅ ICF **Wheel Specification** form submissions
- ✅ ICF **Bogie Checksheet** form submissions
- ✅ Secure **JWT-based Authentication**
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ Optional Docker support

## 🔧 Technologies Used
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (PyJWT)
- CORS Middleware
- Uvicorn
- Python 3.9+

## 📂 Project Structure
```
app/
├── main.py                # FastAPI app entry point
├── models.py              # SQLAlchemy ORM models
├── schemas.py             # Pydantic schemas
├── database.py            # DB connection
├── routers/
│   ├── auth.py            # Login & Registration
│   ├── wheel_spec.py      # Wheel Spec endpoints
│   └── bogie_check.py     # Bogie Checksheet endpoints
.env                       # Environment variables
```

## ✅ Features Implemented

### 1. JWT Authentication
- Endpoint: `POST /auth/login`
- Accepts: `mobile`, `password`
- Returns: JWT token for access

### 2. Wheel Specification Form
- Endpoint: `POST /wheel/`
- Requires JWT in Authorization header
- Accepts detailed measurement values
- Auto-generates unique `formNumber`
- Stores in PostgreSQL

### 3. Bogie Checksheet Form
- Endpoint: `POST /bogie/`
- Requires JWT
- Accepts `bogieDetails`, `bogieChecksheet`, `bmbcChecksheet`
- All data stored in structured JSON

## 🧪 Testing
Tested using Postman:
- ✅ Successful login returns token
- ✅ `200 OK` on valid Wheel Spec & Bogie submissions
- ✅ `422` or `401` errors handled gracefully
- ✅ Duplicate `formNumber` prevented (unique constraint)

## 🌐 Flutter Frontend Integration
This backend was integrated with a Flutter frontend:
- Wheel and Bogie forms submit to API
- Summary screens update upon success
- Login token is stored using `SharedPreferences`
- Tested with real-time form submission demo

## 🚀 Running Locally

### Step 1: Clone this repo
```bash
git clone https://github.com/yourusername/kpa-backend.git
cd kpa-backend
```

### Step 2: Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Step 3: Set environment variables in `.env`
```
DATABASE_URL=postgresql://<user>:<password>@localhost/<dbname>
JWT_SECRET_KEY=your-secret
```

### Step 4: Run Server
```bash
uvicorn app.main:app --reload
```

## 🐳 Docker (Optional)
Dockerize with:
```bash
docker build -t kpa-backend .
docker run -p 8000:8000 kpa-backend
```

## 📅 Submission Date
> July 22, 2025

---

## 👤 Author
**Aby Daniel Varghese**

> This project was built as part of the Sarva Suvidhaen backend evaluation.
