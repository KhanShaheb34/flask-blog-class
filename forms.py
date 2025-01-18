from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[
                       DataRequired(), Length(min=2, max=20)])
    email = EmailField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
