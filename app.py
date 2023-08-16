from flask import Flask

app = Flask("My web application")


@app.route("/")
@app.route("/index")
def hello_flask():
    return "Hello from Flask!"


@app.route("/login")
def login_page():
    return "You are on login page!"


app.run(debug=True)
