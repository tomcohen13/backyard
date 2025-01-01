import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables from a .env file
load_dotenv()

# Determine the configuration to use
env_name = os.getenv('FLASK_ENV', 'development').lower()

if env_name not in ["development", "production", "testing"]:
    raise ValueError(f"Invalid FLASK_ENV value: {env_name}")

# Create the app
app = create_app(env_name)

if __name__ == "__main__":
    # Run the app
    app.run(
        host=os.getenv('FLASK_RUN_HOST', '127.0.0.1'),
        port=int(os.getenv('FLASK_RUN_PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', 'False') == 'True'
    )
