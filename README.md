# 📝 Blog API - FastAPI Project

This is a simple and secure Blog API built with **FastAPI**, **SQLAlchemy**, **JWT Authentication**, and **SQLite**.

## 🚀 Features

- ✅ User Registration & Login (with JWT)
- ✅ Protected Routes for Authenticated Users
- ✅ CRUD operations for Blog Posts
- ✅ SQLite Database with SQLAlchemy ORM
- ✅ Pydantic Schemas for Validation
- ✅ Swagger UI Documentation at `/docs`
- ✅ Modular Code Structure
- ✅ JWT-Based Authorization (Coming Soon)

---

## 🔐 Authentication

Uses **JWT Tokens** for login sessions.

- `POST /register` - Create a new user
- `POST /login` - Get JWT token
- Pass the JWT token as a Bearer Token in `Authorization` header

---

## 📦 API Endpoints

| Method | Endpoint           | Description                   | Auth Required |
|--------|--------------------|-------------------------------|---------------|
| POST   | `/register`        | Register new user             | ❌ No         |
| POST   | `/login`           | Login and get JWT token       | ❌ No         |
| GET    | `/posts`           | List all posts                | ✅ Yes        |
| POST   | `/posts`           | Create a new post             | ✅ Yes        |
| GET    | `/posts/{id}`      | Get a post by ID              | ✅ Yes        |
| PUT    | `/posts/{id}`      | Update a post (owner only)    | ✅ Yes        |
| DELETE | `/posts/{id}`      | Delete a post (owner only)    | ✅ Yes        |

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Python-Jose (JWT)

---

## 📂 Project Structure

blog-api/
│
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── database.py # SQLAlchemy setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # DB operations
│ ├── auth.py # JWT logic
│ ├── routes/
│ ├── users.py
│ └── posts.py
│
├── README.md
├── requirements.txt
└── .env.example # (Optional) for secrets

yaml
Copy
Edit

---

## 🚀 Getting Started Locally

```bash
# 1. Clone the repo
git clone https://github.com/Mohitkundu360/blog-api.git
cd blog-api

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn app.main:app --reload
📚 API Docs
Swagger: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

✅ To Do
 JWT Authorization on PUT & DELETE (only owner)

 Add Unit Tests using pytest

 Add Pagination to /posts

 Optional Postman Collection or Swagger Screenshot

👨‍💻 Author
Mohit Kundu
GitHub Profile

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### ✅ Next Step

1. Save this as `README.md` in your project root.
2. Then run these commands to commit it:

```bash
git add README.md
git commit -m "📝 Add README file"
git push origin main