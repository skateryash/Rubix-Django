# CubeClasses Course Management

A web-based course management application built with Django, providing functionalities to manage courses, user registration, authentication, and API endpoints for external integrations. This project includes a user-friendly interface for managing courses and their details, along with a fully functional API.

## Features

- **Course Management**: Add, update, delete, and view course details.
- **Pagination**: Easily browse through a paginated list of courses.
- **API Integration**: REST API for external integration to add, update, edit, delete, and list courses.
- **User Authentication**: Token-based authentication with registration and login.
  
## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, Django templates
- **Database**: SQLite (for development)
- **Authentication**: Token Authentication using Django REST Framework's Token system

## Installation and Setup

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework

### Step 1: Clone the Repository

```bash
git clone https://github.com/skateryash/API-Task.git
cd API-Task
```

### Step 2: Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

```bash
python manage.py migrate
```

### Step 5: Create a Superuser

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## Project Structure

```bash
cubeclasses/
    ├── cubeclasses/         # Main project directory
    ├── course/              # Course management app
    │   ├── migrations/      # Database migrations
    │   ├── templates/       # HTML templates for frontend
    │   ├── views/           # Views for handling web requests and APIs
    │   └── models.py        # Database models for Courses
    ├── manage.py            # Django management script
    ├── requirements.txt     # Project dependencies
    └── README.md            # Project documentation
```

## API Endpoints

The project exposes several REST API endpoints for managing courses. Here's a summary of the key API endpoints:

- **List all courses**: `GET /course/api/index/`
- **Add a course**: `POST /course/api/add/`
- **Edit a course**: `PATCH /course/api/edit/`
- **Update a course**: `PUT /course/api/update/`
- **Delete a course**: `DELETE /course/api/delete/`

### Example API Requests:

#### List Courses

```bash
GET /course/api/index/
```

#### Add a Course

```bash
POST /course/api/add/
{
  "name": "New Course",
  "description": "Course description",
  "level": "Beginner",
  "mode": "Online"
}
```

#### Edit a Course

```bash
PATCH /course/api/edit/
{
  "id": 1,
  "name": "Updated Course Name"
}
```

## Screenshots

![Screenshot (5)](https://github.com/user-attachments/assets/1749daf5-40d8-4cc6-8b7b-f75ce6081053)

![Screenshot (6)](https://github.com/user-attachments/assets/8706cb28-f6ff-42ba-96f9-1799fcfe3a60)

![Screenshot (7)](https://github.com/user-attachments/assets/05e400f0-0060-419a-8902-eb809e249ae6)

![Screenshot (8)](https://github.com/user-attachments/assets/562f9bd1-e26c-4170-9e54-33426a6533ba)

![Screenshot (9)](https://github.com/user-attachments/assets/a04f8662-acb6-4305-85f9-8027a4df44f2)

![Screenshot (10)](https://github.com/user-attachments/assets/4ce20612-a413-4ed2-841f-772b62b82e05)

![Screenshot (11)](https://github.com/user-attachments/assets/c54c87ae-ba0c-4a86-9f55-39f0cffc370e)

