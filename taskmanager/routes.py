from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    # This queries the imported category, retrieves all records and sorts them by name. the all MUST go at the end.
    # list() converts the cursor object to a python list
    categories = list(Category.query.order_by(Category.category_name).all())
    # categories=categories. The first one is the variable name we can use in the categories html. The second one is the variable in the line above this.
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
# NB: IN THE REAL WORLD THIS WOULD HAVE SOME DEFENSIVE PROGRAMMING AND ERROR HANDLING
def add_category():
    # This sets the post method to allow users to add category to the database
    if request.method == "POST":
        # Create new category variable
        # copy the variable from the model to make sure it's right (category_name)
        # Set it to the value of the input from the form
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        # When someone adds a category, redirect them to the updated categories page
        return redirect(url_for("categories"))
    return render_template("add_category.html")
