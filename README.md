# Book-Store

Bookstore is a full-featured application for managing books, providing secure authentication and complete CRUD functionality. It is built with modern technologies and ensures reliable data handling and validation.

## Technologies Used

- Python  
- FastAPI  
- PostgreSQL  
- JWT  

## Setup Guide

### Clone the Repository

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

### Backend Setup

1. **Create and activate a virtual environment:**

```bash
uv venv
source .venv/bin/activate
```

2. **Install dependencies:**

```bash
uv sync
```

3. **Create a `.env` file in the backend root directory with the following content:**

```env
DB_URL=postgresql://username:password@localhost:5432/dbname
CORS_ORIGIN=*
SECRET_KEY=your_jwt_secret
```

4. **Start the backend server:**

```bash
uv run uvicorn src.backend.main:app --reload
```

### Access the App

- Backend API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
