import os
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
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# Create an instand of the imported alchemy class
db = SQLAlchemy(app)

from taskmanager import routes  # noqa