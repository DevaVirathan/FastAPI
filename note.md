
###### FastAPI ######

# 1. What is FastAPI?

FastAPI is a modern, fast (high-performance) Python web framework for building APIs. It uses Python type hints and automatic validation powered by Pydantic.

# 2. Why it's used

Build APIs quickly.
Automatic request validation.
Automatic OpenAPI schema generation.
Automatic interactive documentation (/docs and /redoc).

# 3. Installation

pip install fastapi uvicorn[standard]

# 4. Run the server

uvicorn main:app --reload

# 5. Example Use Cases

Microservices
Backend for mobile apps/websites
Machine learning model serving
CRUD applications

Code:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

# 6. How it works

FastAPI() creates an app instance.
@app.get("/") defines a route that listens to GET requests.
Function returns JSON automatically.

# 7. Path Operations (Routes)

A path operation defines what your API should do when the client hits a specific path (URL) using a specific HTTP method.
Example:
| Method | Purpose          |
| ------ | ---------------- |
| GET    | Read data        |
| POST   | Create data      |
| PUT    | Replace data     |
| PATCH  | Update partially |
| DELETE | Remove data      |

# 8. Request Body (Pydantic Model)

Data the client sends (example: user registration form). FastAPI uses Pydantic models for validation and structure.

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/register")
def register_user(user: User):
    return {"message": "User registered", "data": user}

# 9. Query Parameters

Optional or additional values passed in the URL after ?.
Example URL : /products?limit=10&search=phone

@app.get("/products")
def list_products(limit: int = 10, search: str | None = None):
    return {"limit": limit, "search": search}

How it works

limit=10 → default value.

search is optional (None allowed).

# 10. Path Parameters

Variables inside the URL path.
/users/1

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

How it works

{user_id} captured from URL.
Automatically converted to int.

# 11. Status Codes
HTTP status codes tell whether request succeeded or failed.

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 400  | Bad Request  |
| 404  | Not Found    |
| 500  | Server Error |

from fastapi import status

@app.post("/login", status_code=status.HTTP_201_CREATED)
def login():
    return {"message": "Logged in"}

# 12. Response Models

Response models control what data is returned to the client.

class UserResponse(BaseModel):
    id: int
    name: str

@app.get("/profile", response_model=UserResponse)
def profile():
    return {"id": 1, "name": "Alice", "password": "secret"}

How it works : 
Removes extra fields like password.

# 13. Error Handling

from fastapi import HTTPException

@app.get("/items/{id}")
def get_item(id: int):
    if id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": id}

# 14. Dependency Injection

A way to share reusable logic (database connection, auth checks).
from fastapi import Depends

def get_token():
    return "super-secret-token"

@app.get("/secure")
def secure_route(token: str = Depends(get_token)):
    return {"token": token}

# 15. FastAPI with Database

users = []

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User added"}

@app.get("/users")
def get_all_users():
    return users

# 16. Folder Structure :

project/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── routes/
│   │   │   │   ├── users.py
│   │   │   │   ├── auth.py
│   │   │   │   └── tasks.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   │
│   ├── db/
│   │   ├── base_class.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── user.py
│   │       └── task.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   └── task_service.py
│   │
│   ├── repositories/
│   │   ├── user_repo.py
│   │   └── task_repo.py
│   │
│   ├── utils/
│   │   ├── hash.py
│   │   └── jwt.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── __init__.py
│
├── alembic/
│   └── migrations/
│
├── .env
├── requirements.txt
├── Dockerfile
└── README.md


