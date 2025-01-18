from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "my_secret_key"

messages = []


@app.route("/")
def home():
    return render_template("home.jinja")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        messages.append(f"{name}: {email} sent: {message}")

        flash(f"Thanks for message {name}", "success")
        return redirect(url_for("contact"))

    return render_template("contact.jinja", form=form, messages=messages)


if __name__ == "__main__":
    app.run(debug=True)
