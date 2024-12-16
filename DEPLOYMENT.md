
# Deployment Instructions

## Using Docker
1. Build the Docker image:
   ```bash
   docker build -t fitness-tracker .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 fitness-tracker
   ```

## Without Docker
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables for production in a `.env` file:
   ```env
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=yourdomain.com,localhost
   DATABASE_URL=postgres://username:password@hostname:port/databasename
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   gunicorn fitness_project.wsgi:application --bind 0.0.0.0:8000
   ```
