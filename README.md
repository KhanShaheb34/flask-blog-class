# Chapter 1: Introduction & Overview

## 1.1 What is Flask and Why Use It?

**Flask** is a lightweight web framework for Python. It’s called a “micro” framework because it doesn’t require particular tools or libraries and doesn’t impose a specific project layout. This flexibility makes Flask popular for small-to-medium projects—and even some large-scale ones—because you can add only the extensions you need (e.g., for databases, authentication, form handling, etc.).

**Key Advantages**:

1. **Simplicity**: Very little boilerplate code; you can start small.
2. **Flexibility**: You are free to choose databases, libraries, or structure.
3. **Active Community**: Many available plugins/extensions (Flask-Login, Flask-Migrate, etc.).
4. **Well-Documented**: Excellent official docs and plenty of tutorials/examples.

**Why use Flask for this blog application?**

- It’s perfect for teaching the fundamentals of HTTP, routing, request handling, and templating without overhead.
- It’s straightforward enough that new learners can see results quickly (“Hello World” in just a few lines of code).

## 1.2 Project Overview (the “Blog” Idea)

We’ll build a blog application with the following features:

- **User Registration & Login** (Authentication)
- **Creating and Managing Posts** (CRUD Operations)
- **User Profiles & Image Upload** (including a profile picture)
- **Database Integration** using **PostgreSQL** for storing users, posts, etc.
- **Styling** with **Bootstrap** to make the app look neat and professional

The end goal:

- A user can register an account, log in, and see a homepage of blog posts.
- A user can create, update, or delete their own posts.
- Users have profile pages where they can update details and upload a profile picture.

## 1.3 Required Tools & Technologies

1. **Python 3.7+** (preferably 3.9 or higher to keep up with latest features)
2. **Flask** (the core framework we’ll use)
3. **PostgreSQL** (relational database)
4. **Bootstrap** (CSS framework for styling)
5. A code editor (VSCode, PyCharm, or your preference)
6. Git (version control; recommended but not mandatory for the tutorial)

> **Note**: We’ll eventually deploy to a **Google Cloud VPC**, but that comes later.

## 1.4 Installing Flask

Make sure you have Python 3 installed. You can verify with:

```bash
python --version
```

or

```bash
python3 --version
```

Install Flask using `pip`:

```bash
pip install flask
```

Or, if you have multiple versions of Python and pip, you might need:

```bash
python3 -m pip install flask
```

For reference, see the [Flask Installation Guide](https://flask.palletsprojects.com/en/latest/installation/).

## 1.5 Basic Flask “Hello World”

Let’s create a simple Flask application to verify everything is working.

1. Create a new folder, e.g. `my_blog`.
2. Inside `my_blog`, create a file named `app.py`.
3. Add the following code to `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    # Turn on debug mode only in development, not in production
    app.run(debug=True)
```

4. Run the app:
   ```bash
   python app.py
   ```
   This starts a local development server, by default on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).  
   You should see “Hello, Flask!” in your browser when you visit that URL.

**That’s it**—you now have a minimal Flask application up and running!

# Chapter 2: Project Setup & Basic Structure

At this point, we know how to create a basic Flask app. Next, we’ll discuss **project structure**, **virtual environments**, and **static & templates folders**, so our project is ready for growth.

## 2.1 Virtual Environments & Dependency Management

A **virtual environment** ensures that your project’s Python libraries (Flask, SQLAlchemy, etc.) are isolated from system-wide Python installations. This avoids version conflicts and keeps your project self-contained.

1. **Create a virtual environment** (using the built-in `venv` module):

   ```bash
   python -m venv venv
   ```

   This creates a folder named `venv` in your project directory (you can name it anything you want).

2. **Activate the virtual environment**:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Flask in this environment**:

   ```bash
   pip install flask
   ```

4. **Verify** that Flask is installed:

   ```bash
   pip list
   ```

5. **Add a requirements file**:  
   It’s a good practice to have a `requirements.txt` or `Pipfile` (if using Pipenv). For now:
   ```bash
   pip freeze > requirements.txt
   ```
   This will record all installed dependencies, which helps when sharing the project or deploying.

> **Tip**: When you’re done working, you can deactivate with:
>
> ```bash
> deactivate
> ```

## 2.2 Ideal Folder Structure (Starting Simple)

Flask doesn’t enforce a strict structure, but here’s a recommended layout for a small-to-medium project:

```
my_blog/
│
├── app.py                  # Entry point (will evolve later)
├── requirements.txt        # Dependencies
├── venv/                   # Virtual environment (not checked into git)
│
├── static/                 # CSS, JavaScript, images
├── templates/              # HTML templates (Jinja2)
│
└── .gitignore              # Optional, for git version control
```

We’ll **later** move to a package structure (with an `app` folder, `__init__.py`, Blueprints, etc.). But starting with a single-file `app.py` + `static/` + `templates/` helps you learn the basics before we refactor.

## 2.3 Running Your Flask App

From the `my_blog` directory, ensure your virtual environment is active, then:

```bash
python app.py
```

Open a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000). You’ll see your “Hello World” (or “Hello, Flask!”) message.

**Alternative**:  
You can also set environment variables and use the `flask run` command. For example:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

- `FLASK_APP=app.py` tells Flask which file to run.
- `FLASK_ENV=development` enables debug mode, which restarts your server automatically on file changes and shows helpful debug messages.

_(On Windows, you’d typically use `set FLASK_APP=app.py` in Command Prompt or `$env:FLASK_APP="app.py"` in PowerShell.)_

## 2.4 Serving Static Files & Templates

**Static Files** (e.g. CSS, JavaScript, images) go in the `static/` directory by default. Flask automatically knows to look in `static/`.

**HTML Templates** go in the `templates/` directory. We’ll use the [Jinja2 templating engine](https://jinja.palletsprojects.com/) to render dynamic data.

**Example**:  
If you have `templates/index.html`, you can render it like so:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Looks in templates/index.html
```

This `index.html` can reference a static file, say `style.css`, in `static/`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

## 2.5 Introduction to Bootstrap for Quick UI Styling

[Bootstrap](https://getbootstrap.com/) is a popular CSS framework. It helps you create a responsive layout and provides pre-styled components (buttons, navbars, forms, etc.).

To use Bootstrap in your Flask templates:

1. **Download** Bootstrap files or link via CDN.
2. In your `templates/layout.html` (we’ll create a base layout soon), include the Bootstrap CSS and JS links:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <title>My Flask Blog</title>
       <!-- Bootstrap CSS (CDN) -->
       <link
         rel="stylesheet"
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
       />
     </head>
     <body>
       <div class="container">{% block content %} {% endblock %}</div>

       <!-- Bootstrap JS (CDN) -->
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
     </body>
   </html>
   ```

3. Create other template files (e.g., `index.html`) that **extend** this layout:

   ```html
   {% extends "layout.html" %} {% block content %}
   <h1>Hello, Flask with Bootstrap!</h1>
   {% endblock %}
   ```

# Chapter 3: Working with Templates & Static Files

## 3.1 Jinja2 Template Basics

**Jinja2** is Flask’s default templating engine. It allows you to generate dynamic HTML pages by mixing Python-like expressions and logic into your HTML files.

### Key Concepts in Jinja2

1. **Expressions**:

   ```html
   {{ variable_name }}
   ```

   This outputs the value of `variable_name`.

2. **Control Structures**:

   ```html
   {% if condition %}
   <p>Condition is true!</p>
   {% endif %}
   ```

   or

   ```html
   {% for item in items %}
   <li>{{ item }}</li>
   {% endfor %}
   ```

   This is how you handle loops, conditionals, etc.

3. **Template Inheritance**:
   - A **base template** (e.g., `layout.html`) contains common HTML (header, footer, nav).
   - **Child templates** can “extend” that base and override specific sections (e.g., main content).

### Why Use Jinja2?

- It separates **presentation** (HTML/CSS) from **logic** (Python).
- It’s a secure way to render data (it escapes special characters to prevent XSS attacks by default).
- It keeps your code organized; you don’t mix HTML strings into your Python code.

---

## 3.2 Handling CSS and JS in Flask

### 3.2.1 Static Folder Recap

In Chapter 2, we created a `static/` folder. By default, Flask knows to look here for static files like CSS, JavaScript, or images. If you have `static/style.css`, you can reference it in a Jinja2 template using:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

**`url_for('static', filename='...')`** generates a correct URL path to that static file, respecting the environment (development or production).

### 3.2.2 Serving JavaScript Files

Similarly, place a file like `main.js` in your `static/` folder:

```
my_blog/
├── static/
│   ├── style.css
│   └── main.js
...
```

Then reference it in your template:

```html
<script src="{{ url_for('static', filename='main.js') }}"></script>
```

### 3.2.3 Using External Libraries (e.g., Bootstrap via CDN)

We often use a **Content Delivery Network (CDN)** for libraries like Bootstrap, jQuery, or Font Awesome. This means you don’t need to download them manually; just include a `<link>` or `<script>` tag pointing to the CDN.

For Bootstrap 5, for example:

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
/>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

---

## 3.3 Creating a Simple Homepage (layout.html, index.html)

### 3.3.1 Setting Up `layout.html` (Base Template)

A **layout** (or base) template holds common HTML elements such as:

- **`<head>`** with meta tags, title, link to CSS files
- A **navbar** or **header** that appears on every page
- A **footer** if desired

Create `templates/layout.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>My Flask Blog</title>
    <!-- Bootstrap CSS (CDN) -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
    />

    <!-- Your custom CSS -->
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}"
    />
  </head>
  <body>
    <!-- Simple Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="{{ url_for('home') }}">MyBlog</a>
        <!-- Additional nav items if needed -->
      </div>
    </nav>

    <div class="container mt-4">{% block content %} {% endblock %}</div>

    <!-- Bootstrap JS (CDN) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Your custom JS -->
    <script src="{{ url_for('static', filename='main.js') }}"></script>
  </body>
</html>
```

### 3.3.2 Creating `index.html` (Child Template)

In `templates/index.html`:

```html
{% extends "layout.html" %} {% block content %}
<h1>Welcome to My Flask Blog</h1>
<p>This is our homepage content.</p>
{% endblock %}
```

Notice we use:

```html
{% extends "layout.html" %}
```

to inherit from `layout.html` and override the `{% block content %}` section with our homepage text.

### 3.3.3 Updating `app.py`

Let’s create a function to handle the homepage route:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Now, when you navigate to `http://127.0.0.1:5000`, Flask renders `templates/index.html` which in turn extends `templates/layout.html`.

---

## 3.4 Adding Navigation & Base Styling with Bootstrap

### 3.4.1 A Basic Bootstrap Navbar

We already added a simple Navbar in `layout.html`. Let’s enhance it slightly. For example, update the `<nav>` area:

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="{{ url_for('home') }}">MyBlog</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="#">Login</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Register</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

This gives us a more fully-featured, responsive navbar with a toggle button on mobile.

### 3.4.2 Container & Layout Helpers

Inside the `body` of `layout.html`, we wrapped everything in a `<div class="container">`. In Bootstrap, `.container`, `.row`, and `.col-xx` are handy classes to structure your page responsively. For example:

```html
<div class="container mt-4">
  <div class="row">
    <div class="col-md-8">{% block content %} {% endblock %}</div>
    <div class="col-md-4">
      <!-- Sidebar content or ads can go here -->
    </div>
  </div>
</div>
```

### 3.4.3 Customizing with Your Own CSS

In `static/style.css`, you might add:

```css
body {
  background-color: #f8f9fa; /* slightly gray background */
}
```

Since it’s linked in `layout.html`, these styles will apply globally.

---

## Putting It All Together

1. **Directory Structure** (recap):
   ```
   my_blog/
   ├── app.py
   ├── requirements.txt
   ├── static/
   │   ├── style.css
   │   └── main.js
   └── templates/
       ├── layout.html
       └── index.html
   ```
2. **Run Your App**:
   ```bash
   python app.py
   ```
   or
   ```bash
   flask run
   ```
3. **Visit**: [http://127.0.0.1:5000](http://127.0.0.1:5000) to see your new homepage.

# Chapter 4: Forms & Basic Validation

## 4.1 Introduction to Handling Forms in Flask

When building a web app, you’ll often need to gather data from users—like signing up for a newsletter, registering an account, or creating a new post. In Flask, there are two common approaches to handling forms:

1. **Manual Handling**:

   - Write the HTML form in your template.
   - Capture data in your Flask route using `request.form`.
   - Implement your own validation logic (e.g., checking if fields are empty).

2. **Using a Form Library (e.g., WTForms via Flask-WTF)**:
   - WTForms provides a Python class-based approach to building forms.
   - It automatically handles validation, error messages, and CSRF protection (if using Flask-WTF).

**Which approach should you use?**

- For **simple** forms or a quick demo, manual handling is fine.
- For **production-level** apps or more robust validation, **WTForms (Flask-WTF)** is recommended.
- We’ll illustrate both approaches briefly, then lean toward WTForms for best practices.

---

## 4.2 Setting Up a Contact (or Basic) Form

Let’s create a **Contact** page as an example. The same logic applies to any form (like a registration form or a “create post” form).

### 4.2.1 Manual HTML Form (No WTForms)

1. **Add a Route** in `app.py` (or wherever your routes live):

   ```python
   from flask import Flask, render_template, request, redirect, url_for, flash

   app = Flask(__name__)
   app.secret_key = "some_secret_key_here"  # Required for flashing messages

   @app.route('/contact', methods=['GET', 'POST'])
   def contact():
       if request.method == 'POST':
           # Retrieve form data
           name = request.form.get('name')
           email = request.form.get('email')
           message = request.form.get('message')

           # Basic validation
           if not name or not email or not message:
               flash("All fields are required.", "error")
               return redirect(url_for('contact'))

           # In a real app, you might send an email or store the message
           flash("Thanks for contacting us!", "success")
           return redirect(url_for('contact'))

       return render_template('contact.html')
   ```

2. **Create `contact.html`** in your `templates/` folder:

   ```html
   {% extends "layout.html" %} {% block content %}
   <h1>Contact Us</h1>

   <!-- Display flashed messages -->
   {% with messages = get_flashed_messages(with_categories=true) %} {% if
   messages %} {% for category, msg in messages %}
   <div class="alert alert-{{ category }}">{{ msg }}</div>
   {% endfor %} {% endif %} {% endwith %}

   <form method="POST" action="{{ url_for('contact') }}">
     <div class="mb-3">
       <label for="name" class="form-label">Name</label>
       <input type="text" class="form-control" id="name" name="name" />
     </div>
     <div class="mb-3">
       <label for="email" class="form-label">Email</label>
       <input type="email" class="form-control" id="email" name="email" />
     </div>
     <div class="mb-3">
       <label for="message" class="form-label">Message</label>
       <textarea
         class="form-control"
         id="message"
         name="message"
         rows="3"
       ></textarea>
     </div>
     <button type="submit" class="btn btn-primary">Submit</button>
   </form>
   {% endblock %}
   ```

3. **Add a Navbar Link** (optional) in `layout.html` to reach `contact`:
   ```html
   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
     <div class="container">
       <a class="navbar-brand" href="{{ url_for('home') }}">MyBlog</a>
       <div class="collapse navbar-collapse" id="navbarSupportedContent">
         <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
           <li class="nav-item">
             <a class="nav-link" href="{{ url_for('home') }}">Home</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
           </li>
         </ul>
       </div>
     </div>
   </nav>
   ```
4. **Test** the form by navigating to `http://127.0.0.1:5000/contact`.

### 4.2.2 Using WTForms (via Flask-WTF)

Next, let’s see how to use **WTForms** for better organization and validation.

1. **Install** the library:
   ```bash
   pip install flask-wtf
   ```
2. **Create a Form Class** in a new file, e.g. `forms.py`:

   ```python
   from flask_wtf import FlaskForm
   from wtforms import StringField, TextAreaField, SubmitField
   from wtforms.validators import DataRequired, Email

   class ContactForm(FlaskForm):
       name = StringField('Name', validators=[DataRequired()])
       email = StringField('Email', validators=[DataRequired(), Email()])
       message = TextAreaField('Message', validators=[DataRequired()])
       submit = SubmitField('Submit')
   ```

3. **Update `app.py`**:

   ```python
   from flask import Flask, render_template, flash, redirect, url_for
   from forms import ContactForm

   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'some_secret_key_here'

   @app.route('/contact', methods=['GET', 'POST'])
   def contact():
       form = ContactForm()
       if form.validate_on_submit():
           # If form is valid, you can access form.data or form fields
           name = form.name.data
           email = form.email.data
           message = form.message.data
           # Do something with the data (e.g., send email, save to DB)
           flash('Thanks for contacting us!', 'success')
           return redirect(url_for('contact'))

       return render_template('contact.html', form=form)
   ```

4. **Modify `contact.html`** for WTForms:

   ```html
   {% extends "layout.html" %} {% block content %}
   <h1>Contact Us (WTForms)</h1>

   {% with messages = get_flashed_messages(with_categories=true) %} {% if
   messages %} {% for category, msg in messages %}
   <div class="alert alert-{{ category }}">{{ msg }}</div>
   {% endfor %} {% endif %} {% endwith %}

   <form method="POST" action="{{ url_for('contact') }}">
     {{ form.hidden_tag() }}
     <!-- CSRF protection -->

     <div class="mb-3">
       {{ form.name.label(class_='form-label') }} {{
       form.name(class_='form-control') }} {% for error in form.name.errors %}
       <div class="text-danger">{{ error }}</div>
       {% endfor %}
     </div>

     <div class="mb-3">
       {{ form.email.label(class_='form-label') }} {{
       form.email(class_='form-control') }} {% for error in form.email.errors %}
       <div class="text-danger">{{ error }}</div>
       {% endfor %}
     </div>

     <div class="mb-3">
       {{ form.message.label(class_='form-label') }} {{
       form.message(class_='form-control') }} {% for error in
       form.message.errors %}
       <div class="text-danger">{{ error }}</div>
       {% endfor %}
     </div>

     {{ form.submit(class_='btn btn-primary') }}
   </form>
   {% endblock %}
   ```

5. **Run your app** and test the form:
   - If you leave fields empty or type an invalid email, WTForms will show validation errors.
   - Submitting a valid form will flash a success message.

---

## 4.3 Client-Side vs. Server-Side Validation

- **Server-Side Validation** (via WTForms or manual checks) is critical for security. It ensures that malicious users or bots can’t bypass rules just by disabling JavaScript.
- **Client-Side Validation** can provide a better user experience by catching errors early (e.g., “Please enter a valid email” messages before form submission). However, it’s never a substitute for server-side checks.

**Tip**: You can combine both. Use **HTML5 attributes** (like `required`, `type="email"`) and/or **JavaScript** for quick feedback, but always confirm in Python on the server.

---

## 4.4 Rendering Errors in Templates

We’ve seen two methods of showing errors:

1. **Flask’s `flash` function** (suitable for quick messages or manual validation errors).
2. **WTForms Field Errors** (each field tracks its own validation errors, which you display next to the field).

**Best Practice**: Keep error messages near the form fields that need correcting. This is more user-friendly and helps them quickly fix mistakes.

---

## 4.5 Building a Dynamic Homepage (Optional Early Demo)

If you want to see the form submissions displayed on the homepage (just as a demo), you could:

1. Create a global list or dictionary to store form submissions (in memory).
2. Display them dynamically on `index.html`.

**Example** (in `app.py`):

```python
submissions = []

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        data = {
            'name': form.name.data,
            'email': form.email.data,
            'message': form.message.data
        }
        submissions.append(data)
        flash("Thanks for your submission!", 'success')
        return redirect(url_for('home'))  # or 'contact'

    return render_template('contact.html', form=form)

@app.route('/')
def home():
    return render_template('index.html', submissions=submissions)
```

Then, in `index.html`:

```html
{% extends "layout.html" %} {% block content %}
<h1>Homepage</h1>
<ul>
  {% for sub in submissions %}
  <li><strong>{{ sub.name }}</strong> - {{ sub.email }}: {{ sub.message }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

Of course, this is just an **in-memory** approach—once the server restarts, the data is lost. Later chapters will show how to store data permanently in **PostgreSQL**.
