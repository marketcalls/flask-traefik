# Flask Application with Traefik Reverse Proxy

This project demonstrates a Flask application setup using Traefik as a reverse proxy with Docker containers. The application features blueprints for modular routing, Tailwind CSS for styling, and ProxyFix for secure deployment behind a reverse proxy.

## Prerequisites

- Docker and Docker Compose installed on your system
- Git (optional, for cloning the repository)

### Host Configuration

#### For macOS and Linux:
1. Open Terminal
2. Edit the hosts file using sudo:
   ```bash
   sudo nano /etc/hosts
   ```
3. Add these lines:
   ```
   127.0.0.1 flask.localhost
   127.0.0.1 traefik.localhost
   ```
4. Save the file:
   - Press `Ctrl + X`
   - Press `Y` to confirm
   - Press `Enter` to save

#### For Windows:
1. Open Notepad as Administrator
   - Right-click on Notepad
   - Select "Run as administrator"
2. Open the hosts file:
   - File > Open
   - Navigate to: `C:\Windows\System32\drivers\etc\`
   - Change file type to "All Files"
   - Select the `hosts` file
3. Add these lines:
   ```
   127.0.0.1 flask.localhost
   127.0.0.1 traefik.localhost
   ```
4. Save the file

## Project Structure

```
flask-traefik/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py         # Blueprint routes
│   ├── templates/
│   │   ├── base.html       # Base template with Tailwind CSS
│   │   ├── index.html      # Home page template
│   │   └── about.html      # About page template
│   ├── app.py             # Main application with ProxyFix
│   └── requirements.txt    # Python dependencies
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Flask app container configuration
└── traefik.yaml          # Traefik static configuration
```

## Features

### Flask Application
- Modular routing using Blueprints
- Tailwind CSS for modern, responsive styling
- ProxyFix middleware for secure proxy header handling
- Security headers implementation:
  - HSTS (HTTP Strict Transport Security)
  - Content Security Policy (CSP)
  - X-Frame-Options
  - X-Content-Type-Options
  - X-XSS-Protection

### Traefik Integration
- Version: v3.2.1
- Reverse proxy and load balancer
- Automatic service discovery
- Web dashboard for monitoring
- Secure routing based on hostnames

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
   - Features:
     - Home page with welcome message
     - About page with project details
     - Responsive navigation
     - Modern UI with Tailwind CSS

2. **Traefik Dashboard**:
   - URL: http://traefik.localhost:8080
   - Provides monitoring and management interface for Traefik

## Security Considerations

The application implements several security measures:

1. **ProxyFix Middleware**:
   - Properly handles X-Forwarded-For headers
   - Configures proxy counts for various headers
   - Ensures correct client IP resolution

2. **Security Headers**:
   - HSTS for enforcing HTTPS
   - CSP for controlling resource loading
   - X-Frame-Options to prevent clickjacking
   - X-Content-Type-Options to prevent MIME-type sniffing
   - X-XSS-Protection for cross-site scripting protection

## Dependencies

Python packages required for the Flask application:
- Flask==3.1.0
- gunicorn==23.0.0
- Werkzeug==3.1.3 (includes ProxyFix)
- Other supporting packages listed in requirements.txt

## Notes

- This setup includes development-mode settings (like exposed Traefik dashboard)
- For production deployment:
  - Enable HTTPS
  - Configure stricter security policies
  - Adjust ProxyFix settings based on your proxy setup
  - Implement proper authentication
- The Flask application demonstrates basic features and can be extended based on requirements
