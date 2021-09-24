import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import env to use our hidden environment variables
if os.path.exists("env.py"):
    import env  # noqa <- this removes linting warning

# Create an instance of the imported Flask class
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == TRUE:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri # heroku

# Create an instand of the imported alchemy class
db = SQLAlchemy(app)

from taskmanager import routes  # noqa