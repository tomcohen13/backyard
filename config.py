import os
import secrets

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    UPLOAD_FOLDER = "static/uploads"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # Limit uploads to 2MB


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SERVER_NAME = os.getenv("SERVER_NAME", "the-backyard.herokuapp.com")

    if not os.getenv("SECRET_KEY"):
        raise ValueError("SECRET_KEY environment variable is not set in production!")
