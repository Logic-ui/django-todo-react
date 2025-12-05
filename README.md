# Todo App

A full-stack Todo application built with **Django REST Framework** for the backend and **React.js** for the frontend. This app allows users to create, edit, delete, and mark tasks as completed. The project is fully containerized using **Docker** and supports PostgreSQL as the database.

---

## Features

- Create, update, and delete todo items
- Mark tasks as completed or incomplete
- Filter tasks by status (completed/incomplete)
- Responsive UI built with React and Bootstrap 4
- REST API powered by Django REST Framework
- JWT-based authentication support (via `djangorestframework-simplejwt`)
- Dockerized setup for development and deployment

---

## Technologies Used

### Backend
- Python 3.9
- Django 4.x
- Django REST Framework
- PostgreSQL
- Gunicorn
- Docker

### Frontend
- React.js
- Bootstrap 4
- Axios (for API requests)
- Reactstrap (for modals)

---

## Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Git

---

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Logic-ui/django-todo-react.git
cd django-todo-react
```

2. **Build and run the Docker containers:**

```bash
docker-compose up --build
```

This will start three services:

- **db**: PostgreSQL database
- **backend**: Django API on port 8000
- **frontend**: React app on port 3000

---

### API Endpoints

| Endpoint                | Method | Description                  |
|-------------------------|--------|------------------------------|
| `/api/todos/`           | GET    | List all todos               |
| `/api/todos/`           | POST   | Create a new todo            |
| `/api/todos/<id>/`      | PUT    | Update a todo by ID          |
| `/api/todos/<id>/`      | DELETE | Delete a todo by ID          |
| `/api/token/`           | POST   | Obtain JWT token             |
| `/api/token/refresh/`   | POST   | Refresh JWT token            |

---

### Running the App Locally

1. **Frontend:**

```bash
cd frontend
npm install
npm start
```

2. **Backend:**

```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access the frontend at: `http://localhost:3000`  
Access the backend API at: `http://localhost:8000/api/todos/`

---

### Testing

**Backend tests:**

```bash
python manage.py test
```

**Frontend tests:**

```bash
npm test
```

---

### Docker Commands

- **Build containers:** `docker-compose build`
- **Run containers:** `docker-compose up`
- **Stop containers:** `docker-compose down`
- **Run backend shell:** `docker-compose run backend python manage.py shell`
- **Apply migrations:** `docker-compose run backend python manage.py migrate`

---

### Folder Structure

```
django-todo-react/
│
├─ backend/           # Django backend
│  ├─ todo/           # App with models, views, serializers
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ ...
│
├─ frontend/          # React frontend
│  ├─ src/
│  │  ├─ components/ # Modal, etc.
│  │  └─ App.js
│  ├─ Dockerfile
│  └─ package.json
│
└─ docker-compose.yml
```

---

### Notes

- Ensure the `DATABASE_URL` in `docker-compose.yml` matches the database credentials.
- JWT authentication is available but optional; you can disable it for simple testing.
- React app communicates with the backend via Axios. Update `REACT_APP_API_URL` in `.env` if needed.

---

### License

This project is **MIT licensed**.  

---

### Author

**Usman Ali**  
Full-stack developer  

