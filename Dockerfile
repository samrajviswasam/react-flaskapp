# Base Image
FROM python:3.11-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy React application
COPY react-app ./react-app

# Copy Flask application
COPY flaskapp ./flaskapp

# -----------------------
# Build React
# -----------------------
WORKDIR /app/react-app

RUN npm install
RUN npm run build

# -----------------------
# Install Flask Dependencies
# -----------------------
WORKDIR /app/flaskapp

RUN pip install --no-cache-dir -r requirements.txt

# Copy React build into Flask static folder
RUN mkdir -p static
RUN cp -r /app/react-app/build/* static/

# Expose Flask port
EXPOSE 5000

# Start Flask
CMD ["python", "app.py"]
