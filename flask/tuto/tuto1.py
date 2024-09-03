# Youtube: Tech with Tim

from flask import Flask, redirect, url_for

app = Flask(__name__)

# Create page
@app.route("/")
def home():
    return "Xin chào, đây là Homepage <h1>Xin chào<h1>"

@app.route("/<name>")
def user(name):
    return f"Xin chào {name}!"

# web /admin thì sẽ về home
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()

