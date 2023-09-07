from flask import Flask, render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField
from wtforms.validators import DataRequired,InputRequired
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf.csrf import CSRFProtect
import smtplib
import os



# os.getenv()
# user_email = os.environ.get("user_email")
user_email = os.getenv("user_email")
password = os.getenv("password")
# password = os.environ.get("password")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


# flask forms
class Messages(FlaskForm):
    name = StringField('Name',  validators=[DataRequired()])
    email = EmailField("Email",  validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField("Submit")



@app.route("/", methods=["GET", "POST"])
def homepage():
    form = Messages()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        body = form.body.data

        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{body}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user_email, password)
            connection.sendmail(user_email, user_email, email_message)

        with smtplib.SMTP("smtp.gmail.com") as new_connection:
            new_connection.starttls()
            new_connection.login(user_email, password)
            new_connection.sendmail(user_email, email, f"Thank you {name} really appreciate")
        return redirect(url_for("homepage"))


    return render_template("index.html", form=form)



@app.route("/more",methods=["GET", "POST"])
def full_story():
    form = Messages()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        body = form.body.data

        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{body}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user_email, password)
            connection.sendmail(user_email, user_email, email_message)

        with smtplib.SMTP("smtp.gmail.com") as new_connection:
            new_connection.starttls()
            new_connection.login(user_email, password)
            new_connection.sendmail(user_email, email, f"Thank you {name} really appreciate")
        return render_template("homepage")

    return render_template("about.html", form=form)

if __name__ == "__main__":
    app.run(debug=False,  port=8080)
