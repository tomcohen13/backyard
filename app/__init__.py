# Import flask and template operators
from flask import Flask

# Define the WSGI application object
def create_app(env_name: str) -> Flask:
    app = Flask(__name__)

    # Configurations
    app.config.from_object(f"config.{env_name.capitalize()}Config")

    # Import a module / component using its blueprint handler variable (mod_auth)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
