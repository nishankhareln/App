from flask import Flask,render_template,request ,redirect,url_for
import random

app1 = Flask(__name__)

todo_list = []

#route decorator
@app1.route("/")
def index():
    return render_template("result1.html",todo_list = todo_list)

@app1.route("/add",methods = ["POST"])
def add_todo():
    todo = request.form.get("todo")
    if todo:
        todo_list.append(todo)
    return redirect(url_for("index"))

@app1.route("/delete",methods = ["POST"])
def delete_todo():
    todo_index = int(request.form.get("todo_index"))
    if 0 <= todo_index < len(todo_list):
        del todo_list[todo_index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app1.run(debug=True)
