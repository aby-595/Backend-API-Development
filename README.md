# 🚆 Sarva Suvidhaen Backend Assignment – KPA ERP Integration

This project is a complete FastAPI backend implementation for the **ICF Forms API**, built as part of the Sarva Suvidhaen backend evaluation assignment.

## 🎯 Assignment Objective

Develop at least two functional APIs (Wheel Specification and Bogie Checksheet) that:
- Match the provided **Postman collection**, **SwaggerHub docs**, and **Flutter frontend**
- Use **PostgreSQL** for data storage
- Authenticate using a **JWT-based login system**
- Integrate with the existing Flutter app for submission and retrieval

---

## ⚙️ Technologies Used

- **FastAPI** (Backend framework)
- **PostgreSQL** (Database)
- **SQLAlchemy** (ORM)
- **Pydantic** (Data validation)
- **JWT (PyJWT)** (Authentication)
- **Uvicorn** (ASGI Server)
- **CORS Middleware**
- **Python 3.9+**

---

## 📁 Project Structure

```
app/
├── main.py                # FastAPI entry point
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas
├── database.py            # DB connection
├── dependencies.py        # Auth dependency
├── routers/
│   ├── auth.py            # Login / Register
│   ├── wheel_spec.py      # Wheel Spec API
│   └── bogie_check.py     # Bogie Check API
.env                       # Env variables
```

---

## ✅ Features Implemented

### 🔐 1. JWT Authentication

- `POST /auth/login`
- Accepts `mobile` and `password`
- Returns an `access_token`
- Required for all protected routes

### 🛞 2. ICF Wheel Specification

- `POST /wheel/`
- `GET /wheel/`
- Requires valid JWT
- Accepts detailed nested fields
- Auto-saves with `formNumber`, `submittedBy`, and `submittedDate`
- Validated using `Pydantic`

### 🚃 3. ICF Bogie Checksheet

- `POST /bogie/`
- `GET /bogie/`
- Requires JWT
- Accepts complex nested data (bogieDetails, bogieChecksheet, bmbcChecksheet)
- Stores as structured JSON in PostgreSQL

---

## 🧪 Testing with Postman

- ✅ Login returns valid JWT
- ✅ Protected POST routes return 200 OK
- ✅ Form data is saved in PostgreSQL
- ✅ Duplicate `formNumber` prevented
- ✅ Error codes returned for bad/missing data

---

## 📱 Flutter Frontend Integration

- Connected and tested with Flutter UI
- API base URL configured in frontend code
- Forms successfully submitted and summary screens shown
- Token stored via `SharedPreferences` in app

✅ Original Frontend Repo:  
🔗 https://github.com/s2pl/KPA-ERP-FE

✅ My Modified Frontend (with working login):  
🔗 https://github.com/aby-595/KPA-ERP-FE

✅ **API Docs**: [SwaggerHub](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0)

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repo

```bash
git clone https://github.com/aby-595/Backend-API-Development
cd Backend-API-Development
```

### 2. Setup environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure `.env` file

```
DATABASE_URL=postgresql://<user>:aby123@localhost/<kpa-db>
JWT_SECRET_KEY=your-secret-key
```

### 4. Run server

```bash
uvicorn app.main:app --reload
```

---

## 📎 Deliverables

- ✅ Backend source code with two integrated APIs
- ✅ JWT Login system
- ✅ PostgreSQL DB setup
- ✅ Connected and tested with the provided Flutter frontend
- ✅ README with clear setup and documentation
- ✅ Postman collection with working endpoints

---

## 📅 Submission

**Date:** July 22, 2025  
**Author:** Aby Daniel Varghese

> This project was built as part of the Sarva Suvidhaen backend evaluation task.

