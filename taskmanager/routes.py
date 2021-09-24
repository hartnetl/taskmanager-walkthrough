from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

##### CATEGORIES #####

@app.route("/categories")
def categories():
    # This queries the imported category, retrieves all records and sorts them by name when displayed. the all MUST go at the end.
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


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # If we run the file with the router as is, we get a "category undefined" error.
    # We need to create the category variable the template is expecting
    # This variable searches the database for that category id, and returns a 404 error if it does not exist
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        # update the name of the category to whatever was entered by user
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

# Again this needs to know which file to delete so it is passed the category id as an integer and into the function itself
# We can copy a lot from edit above
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    # When we find the file, we delete it and commit the changes
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


##### TASKS #####

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # Each task needs to be assigned a category
    # Here we're calling an ordered list of existing categories, stolen from categories above
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        # these are taken from the models.py schema for tasks
        task = Task(
            # name will be as entered in name field
            task_name=request.form.get("task_name"),
            # description will be as entered in description field
            task_description=request.form.get("task_description"),
            # if urgent is clicked it's urgent, else it's false by default
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            # date set by dtae box
            due_date=request.form.get("due_date"),
            # this will be a dropdown list to choose from exisiting categories
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
        # we must give them the add_task page if they're not posting, and remember to give it categories to access the existing ones
    return render_template("add_task.html", categories=categories)