from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from routes.main import main

def create_app():
    app = Flask(__name__)
    
    # ProxyFix middleware configuration for handling reverse proxy headers
    # Adjust x_for, x_proto, x_host, x_port, x_prefix based on your proxy setup
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,      # Number of proxy servers
        x_proto=1,    # SSL termination proxy
        x_host=1,     # Original host header
        x_port=1,     # Original port
        x_prefix=1    # Proxy path rewriting
    )

    # Security headers
    @app.after_request
    def add_security_headers(response):
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Content-Security-Policy'] = "default-src 'self' https://cdn.tailwindcss.com; script-src 'self' https://cdn.tailwindcss.com 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
        return response

    # Register blueprint
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
