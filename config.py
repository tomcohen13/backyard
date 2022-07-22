# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = "postgresql://lastadbjcgewse:033b8517ddf23df84dcff7ed8e8bf6953e67f15e75b2a61ca35c5eded93bc842@ec2-3-223-169-166.compute-1.amazonaws.com:5432/d72ufh626ddk7p"
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "dBZ-XqxPAfMpS4nqEhAdczv0claN-jHM"

# Secret key for signing cookies
SECRET_KEY = "MitKjYaV9FgUL5zbqqqwWsJ7ADEQ6KTr"