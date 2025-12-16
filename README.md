# E-commerce Backend System (FastAPI + PostgreSQL + Redis)

A simple e-commerce backend built using **FastAPI**, **PostgreSQL**, and **Redis**.  
The system supports cart management, checkout with discount logic, and admin analytics with caching.

---

## 🚀 Features

- RESTful APIs using FastAPI
- Add items to cart
- Checkout with optional discount code
- Discount codes generated every Nth order
- Persistent storage using PostgreSQL
- Redis caching for admin analytics
- Swagger UI & Postman testing support

---

## 🧱 Tech Stack

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL
- **Cache**: Redis
- **ORM**: SQLAlchemy
- **API Testing**: Postman / Swagger UI

---

## 📁 Project Structure

# activate venv (if using)
source venv/Scripts/activate

# install deps
pip install -r requirements.txt

# create tables
python -m app.init_db

# run server
python -m uvicorn app.main:api_ins --reload

