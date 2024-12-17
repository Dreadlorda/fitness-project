
# Deployment Instructions

1. **Build Docker Image**:
   ```bash
   docker build -t fitness_tracker_app .
   ```

2. **Run Docker Container**:
   ```bash
   docker run -p 8000:8000 fitness_tracker_app
   ```

3. Access the app at `http://localhost:8000`.
