from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
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
