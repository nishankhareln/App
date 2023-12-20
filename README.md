//html code for app1.py
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> To-Do List</title>
    <!-- Add Bootstrap CSS link for styling -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f9fa;
            margin: 20px;
        }

        h1 {
            color: #343a40;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            background-color: #fff;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            margin-right: 10px;
        }

        input[type="text"] {
            width: 70%;
            padding: 8px;
            margin-right: 10px;
            border: 1px solid #ced4da;
            border-radius: 4px;
        }

        button {
            padding: 8px 16px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mt-4"> To-Do List</h1>
        
        <ul>
            {% for todo in todo_list %}
                <li>
                    {{ todo }}
                    <form method="post" action="{{ url_for('delete_todo') }}" style="display: inline;">
                        <input type="hidden" name="todo_index" value="{{ loop.index - 1 }}">
                        <button type="submit" class="btn btn-danger btn-sm ml-2">Delete</button>
                    </form>
                </li>
            {% endfor %}
        </ul>

        <form method="post" action="{{ url_for('add_todo') }}" class="mt-3">
            <label for="todo">New Todo:</label>
            <input type="text" id="todo" name="todo" required>
            <button type="submit" class="btn btn-primary">Add</button>
        </form>
    </div>
    <!-- Add Bootstrap JS and Popper.js scripts for additional functionality -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5
