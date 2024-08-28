from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import task_blueprint
from api.resources import api_blueprint
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'

db.init_app(app)

# Register the blueprints
app.register_blueprint(task_blueprint)
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
