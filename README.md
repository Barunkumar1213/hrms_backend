---

# 📕 BACKEND — `README.md`

```md
# HRMS Lite – Backend

## 📌 Project Overview
HRMS Lite Backend is a RESTful API built using FastAPI that supports:
- Employee management
- Attendance tracking
- Duplicate attendance prevention
- Attendance pagination
- Monthly attendance summaries
- MongoDB performance optimization using indexes

The backend serves as the core business logic layer for the HRMS Lite application.

---

## 🧰 Tech Stack Used

- **FastAPI** – Backend framework
- **Python 3.12**
- **MongoDB** – NoSQL database
- **Motor** – Async MongoDB driver
- **PyMongo** – MongoDB utilities & indexing
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server

---

## ▶️ Steps to Run the Backend Locally

### 1️⃣ Prerequisites

Make sure you have:

- Python ≥ 3.10
- MongoDB (local or Atlas)
- Virtual environment support

---

### 2️⃣ Clone & Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows


Install Dependencies

pip install -r requirements.txt


Create a .env file:
MONGO_URI=mongodb://localhost:27017
or MongoDB Atlas URI if using cloud.

5️⃣ Run the Server
uvicorn main:app --reload

6️⃣ API Documentati
http://127.0.0.1:8000/docs

📂 Key API Endpoints
Employees

POST /employees

GET /employees?page=1&limit=5

DELETE /employees/{employee_id}

Attendance

POST /attendance

GET /attendance/{employee_id}


⚡ Database Indexes (Performance)

The backend automatically creates indexes on startup:

Unique compound index on (employee_id, date)

Index on employee_id

Index on date

This ensures:

No duplicate attendance per employee per day

Fast queries even with large datasets

⚠️ Assumptions & Limitations

No authentication or authorization

MongoDB must be running before backend starts

Duplicate records must be cleaned before enabling unique indexes

No soft deletes implemented
```
