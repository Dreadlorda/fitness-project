
# Enhanced Fitness Tracker

This project is a comprehensive fitness tracker built with Django, featuring user authentication, achievements tracking, workouts management, and REST APIs.

## Features
- **CRUD Operations** for Goals, Workouts, and Achievements.
- **Custom Redirect Logic**:
  - Logged-in users are redirected to the **dashboard**.
  - Non-logged-in users are redirected to the **home page** (index).
- **Custom Error Pages**:
  - `404.html`: Page Not Found.
  - `403.html`: Permission Denied.
  - `500.html`: Server Error.
- **REST API Endpoints** for Achievements with Pagination.
- **Admin Dashboard** with advanced filtering, search, and ordering.
- **Interactive Analytics** using Chart.js.

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
4. Run the server:
   ```bash
   python manage.py runserver
   ```

## Deployment
- **Docker Support**: Build and run the containerized project:
   ```bash
   docker build -t fitness-tracker .
   docker run -p 8000:8000 fitness-tracker
   ```
- **Azure Deployment**: Use the `azure_deploy.sh` script for seamless Azure App Service deployment.

## Custom Error Pages
- **404**: User-friendly page for "Page Not Found".
- **403**: Permission denied for restricted content.
- **500**: Server error with a message to try again later.

## Testing
Run tests using the following command:
```bash
python manage.py test
```

## REST API Documentation
Static Swagger documentation is available under `api/swagger_static.yml`. 

## Screenshots
Add screenshots or visuals here to showcase your app.
