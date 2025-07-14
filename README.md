# Codemonk Backend Assignment

This repository contains the backend implementation for the Codemonk Internship Assignment. The project is built using Django and Django REST Framework, with PostgreSQL as the database and Docker for containerization. It provides secure user authentication and APIs for paragraph submission and word indexing.

## Key Features

- JWT-based user authentication
- Auth-protected API access
- Paragraph processing and word indexing
- PostgreSQL database integration
- Docker-based development environment
- Unit testing with Django’s built-in test framework

## Tech Stack

- Python 3.9
- Django 4.2.7
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Git installed

### Setup Instructions

1. **Clone the repository**
   git clone https://github.com/Supriya-G01/codemonk-backend.git
   cd codemonk-backend
2. Configure environment variables

Create a .env file in the project root with the following values:
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=codemonk_db
POSTGRES_USER=codemonk_user
POSTGRES_PASSWORD=codemonk_pass

3. Build and run the application using Docker
docker-compose up --build
4. Apply migrations
docker-compose exec web python manage.py migrate
5. Create a superuser (optional)
docker-compose exec web python manage.py createsuperuser
API Endpoints
Method	Endpoint	Description
POST	/api/token/	Obtain JWT access and refresh tokens
POST	/api/token/refresh/	Refresh JWT access token
GET	/api/test/	Test protected view (requires JWT)
POST	/api/paragraph/	Submit paragraph for indexing
GET	/api/search/?word=	Search for word positions

Authentication
All protected endpoints require an Authorization header with a valid JWT access token:
Authorization: Bearer <access_token>

Running Tests
Run unit tests using the Django test framework:
docker-compose exec web python manage.py test

Project Structure
codemonk-backend/
├── config/              # Project-level settings and configuration
├── core/                # Application logic (views, urls, utils)
├── docker/              # Entrypoint scripts
├── .env                 # Environment variables (not committed)
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Multi-container setup
└── README.md            # Project documentation

License
This project is provided for evaluation as part of a recruitment assignment and is not licensed for production use.
