# Youtube: Tech with Tim

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Create page
@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()

