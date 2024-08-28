from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import task_blueprint
from api.resources import api_blueprint
from extensions import db

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI and the secret key for the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Database file is tasks.db
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Secret key for session management and CSRF protection

# Initialize database with the Flask app
db.init_app(app)

# Register the blueprints for task and API routes
app.register_blueprint(task_blueprint)  # Task-related routes
app.register_blueprint(api_blueprint, url_prefix='/api')  # API routes, prefixed with /api

# Main entry point of the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Start the Flask application with debug mode enabled
