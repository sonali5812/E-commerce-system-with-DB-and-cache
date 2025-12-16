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


## Some screenshots
<img width="1893" height="1093" alt="Screenshot 2025-12-16 200204" src="https://github.com/user-attachments/assets/aa619b5c-f0c4-4dfe-8b02-797156bc3656" />
<img width="1875" height="1051" alt="Screenshot 2025-12-16 200219" src="https://github.com/user-attachments/assets/15b45313-65ea-430a-82fe-648027d8327d" />
<img width="1707" height="1074" alt="Screenshot 2025-12-16 200238" src="https://github.com/user-attachments/assets/5e48e2a3-f2c0-455d-9f66-e24c2c942a2e" />
<img width="1858" height="1027" alt="Screenshot 2025-12-16 200250" src="https://github.com/user-attachments/assets/3e9faeba-61fd-4cea-bb72-0aea5a7a09d8" />
<img width="1885" height="1055" alt="Screenshot 2025-12-16 200437" src="https://github.com/user-attachments/assets/911df5d8-0790-4c7f-bfe9-f0c1c964de49" />
<img width="1899" height="1056" alt="Screenshot 2025-12-16 200452" src="https://github.com/user-attachments/assets/62dde1fc-9966-4593-b77b-eed6a1dc4865" />
<img width="1909" height="1088" alt="Screenshot 2025-12-16 200511" src="https://github.com/user-attachments/assets/3c29ca97-6af4-4ee0-bff4-2d3cfba91440" />
<img width="1879" height="1108" alt="Screenshot 2025-12-16 200344" src="https://github.com/user-attachments/assets/f26c8e99-a0b2-4307-9ec2-ae7079ac8844" />


