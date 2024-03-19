## ToDO App

This a simple ToDo app built with Django

## Instructions to run it:

Create a virtual enviroment and activate it

install django with "pip install Django"

run the migrations with "python Todo/manage.py makemigrations" then "python Todo/manage.py migrate"

run the server with "python Todo/manage.py runserver"


# Features:

    # Index function Route: "":
        It search for every task in the database and pass the list to the template,
        if there's no data, in the template a message would show up to let the user know that is empty.

    # Add function, Route: "add/":
        Initializes a new formModel if the method is GET to send it to the front.
        if the method is Post, it validates the data and saves them.

    # remove function, Route: "remove/id:
        It searchs for the task, if it's found, marks the task as completed and returns the index page.

    # update function, Route: "update/id:
        GET: returns the form populated with the data found from the task_id
        POST: It validates the data, saves them and returns the index page.

    # delete function, Route: "delete/id:
        It takes a task_id as url parameter to search for. if it's found, deletes the task and return the index page.
