from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.jinja")


@app.route("/contact")
def contact():
    return render_template("contact.jinja")


if __name__ == "__main__":
    app.run(debug=True)
