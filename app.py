from flask import Flask, render_template

app = Flask("My web application")


@app.route("/")
@app.route("/index")
def hello_flask():
    return render_template("index.html")


@app.route("/login")
def login_page():
    return "You are on login page!"


@app.route("/user/<username>")
def hello_user(username):
    return render_template("hello.html", username=username)


app.run(debug=True)
