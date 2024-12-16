
# Fitness Tracker Project

A feature-rich fitness tracking application built with Django. This project combines responsive design, role-based access control, and a secure architecture to deliver a scalable fitness tracking solution. Whether you’re managing workouts or tracking nutrition, this application is designed to simplify and enhance your experience.

## Features

### Core Features
- **User Roles**:
  - **Superusers**: Manage users, data, and app settings.
  - **Staff**: Limited admin capabilities with specific permissions.
  - **Regular Users**: Manage their own workouts and nutrition data.
- **Workout Management**:
  - Add, edit, delete, and view workout routines.
- **Nutrition Tracking**:
  - Log and monitor meals with detailed nutritional breakdowns.
- **Role-Based Dashboards**:
  - Separate interfaces for superusers, staff, and regular users.

### Enhanced Functionality
- **Custom Error Pages**:
  - User-friendly `404`, `403`, and `500` pages.
- **REST APIs**:
  - Full API integration for workouts and nutrition tracking using Django REST Framework.
- **Custom Authentication**:
  - Stylish login/logout forms designed with Bootstrap.

### Additional Features
- **Responsive Design**:
  - Mobile-first approach using Bootstrap for seamless access across devices.
- **Security**:
  - Protection against CSRF, XSS, SQL injection, and more.
  - Enforced HTTPS with secure cookies and headers.
- **Asynchronous Views**:
  - Utilizes Django’s async capabilities for high-concurrency scenarios.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite (development) / PostgreSQL (production)
- **Deployment**: Docker, WhiteNoise for static file management

## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/fitness-tracker-project.git
cd fitness-tracker-project
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Migrations
```bash
python manage.py migrate
```

### Seed the Database with Example Users
```bash
python manage.py seed_users
```

### Run the Development Server
```bash
python manage.py runserver
```

## Usage

### Example Users
- **Admin**:
  - Username: `admin`
  - Password: `Admin123!`
- **Staff**:
  - Username: `staff`
  - Password: `Staff123!`
- **Regular User**:
  - Username: `user1`
  - Password: `User123!`

### Available Endpoints
- **Home Page**: `/`
- **Login**: `/login/`
- **Admin Dashboard**: `/admin_dashboard/`
- **Staff Dashboard**: `/staff_dashboard/`
- **User Dashboard**: `/user_dashboard/`
- **Async Demo**: `/async-demo/`
- **REST APIs**:
  - `/api/workouts/`
  - `/api/nutrition/`

## Testing

Run unit and integration tests:
```bash
python manage.py test
```

## Deployment

### Using Docker
- **Build the Docker image**:
  ```bash
  docker build -t fitness-tracker .
  ```
- **Run the container**:
  ```bash
  docker run -p 8000:8000 fitness-tracker
  ```

### Without Docker
Follow the installation instructions above, but configure `.env` with production variables and use Gunicorn:
```bash
gunicorn fitness_project.wsgi:application --bind 0.0.0.0:8000
```

## Project Structure

```plaintext
fitness_tracker_project/
├── fitness_project/        # Main Django project configuration
│   ├── settings/           # Django settings files
│   ├── urls.py             # URL routing
├── users/                  # User management module
│   ├── forms.py            # Custom user forms
│   ├── views.py            # User views
│   ├── mixins.py           # Role-based access mixins
├── workouts/               # Workout tracking module
│   ├── models.py           # Workout models
│   ├── serializers.py      # API serializers
│   ├── views.py            # Workout views
├── nutrition/              # Nutrition tracking module
│   ├── serializers.py      # API serializers
│   ├── views.py            # Nutrition views
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── 404.html            # Custom 404 page
│   ├── 500.html            # Custom 500 page
├── Dockerfile              # Docker configuration
├── DEPLOYMENT.md           # Detailed deployment guide
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Contributing

Pull requests are welcome. For major changes, please open an issue to discuss the proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
