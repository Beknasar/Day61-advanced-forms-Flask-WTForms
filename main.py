from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField

app = Flask(__name__)
app.secret_key = "asuhfsaa-123x2w13fd-12xi3u21890-21we2qwex123"


class LoginForm(FlaskForm):
    email = StringField(label="Email: ")
    password = PasswordField(label="Password: ")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = LoginForm()

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
