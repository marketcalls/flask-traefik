# Flask Application with Traefik Reverse Proxy

This project demonstrates a simple Flask application setup using Traefik as a reverse proxy with Docker containers. The setup includes a basic Flask application serving a "Hello, World!" message and Traefik handling the routing and load balancing.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (optional, for cloning the repository)
- Add the following entries to your `/etc/hosts` file:
  ```
  127.0.0.1 flask.localhost
  127.0.0.1 traefik.localhost
  ```

## Project Structure

```
flask-traefik/
├── app/
│   ├── app.py              # Flask application
│   └── requirements.txt    # Python dependencies
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Flask app container configuration
└── traefik.yaml          # Traefik static configuration
```

## Installation and Setup

1. Clone or download this repository (if applicable)

2. Navigate to the project directory:
   ```bash
   cd flask-traefik
   ```

3. Start the services using Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Verify that the containers are running:
   ```bash
   docker-compose ps
   ```

## Accessing the Services

After starting the services, you can access:

1. **Flask Application**:
   - URL: http://flask.localhost
   - This will display the "Hello, World!" message

2. **Traefik Dashboard**:
   - URL: http://traefik.localhost:8080
   - Provides monitoring and management interface for Traefik

## Components

### Flask Application
- Simple Python web application using Flask
- Runs in a Python 3.9 container
- Served using Gunicorn with 3 workers
- Exposed on port 8000 internally

### Traefik
- Version: v3.2.1
- Acts as a reverse proxy and load balancer
- Provides automatic service discovery
- Features a web dashboard for monitoring
- Handles routing based on hostnames

## Configuration Details

### Docker Compose
- Sets up two services: `traefik` and `flask-app`
- Creates a bridge network for communication
- Configures labels for Traefik routing

### Traefik Configuration
- API and dashboard enabled (insecure mode for demonstration)
- Docker provider enabled
- Web entrypoint configured on port 80
- Automatic service discovery from Docker labels

## Dependencies

Python packages required for the Flask application:
- Flask==3.1.0
- gunicorn==23.0.0
- Other supporting packages listed in requirements.txt

## Notes

- This is a development setup and includes insecure settings (like exposed Traefik dashboard)
- For production use, additional security measures should be implemented
- The Flask application is a minimal example and can be extended based on requirements
