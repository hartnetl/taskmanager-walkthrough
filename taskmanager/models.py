from taskmanager import db


# This project will have two tables, represented using class-based models using 
# SQLAlchemy's ORM

# Data models / schema:

# TABLE 1 for the categories

class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # string(25) sets max character count to 25. 
    # unique = true means each entry must be unique
    # nullable=False sets field as required
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # Link the table to the task table. Wont be visible, just establishes one to many connection
    # lazy=True means that when we query the database for categories, it can simultaneously identify any task linked to the categories.
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string (like 'this' in JS)
        return self.category_name


# TABLE 2 - for the tasks
class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # db.text allows longer strings to be used
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # db.DateTime or db.Time could be used for time with/instead of the date
    due_date = db.Column(db.Date, nullable=False)
    # Add relationship to the category table
    # ondelete="CASCADE" removes the task linked to a category if deleted
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # this is a return for the task class
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )