from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from routes.main import main
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # ProxyFix middleware configuration
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1,
        x_port=1,
        x_prefix=1
    )

    # Get application root from environment variable
    app_root = os.getenv('APPLICATION_ROOT', '/openalgo')
    app.config['APPLICATION_ROOT'] = app_root

    # Security headers
    @app.after_request
    def add_security_headers(response):
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Content-Security-Policy'] = "default-src 'self' https://cdn.tailwindcss.com; script-src 'self' https://cdn.tailwindcss.com 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
        return response

    # Register blueprint with url_prefix from environment
    app.register_blueprint(main, url_prefix=app_root)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
