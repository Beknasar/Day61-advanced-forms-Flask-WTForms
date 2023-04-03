from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "asuhfsaa-123x2w13fd-12xi3u21890-21we2qwex123"


class LoginForm(FlaskForm):
    email = StringField(label="Email: ", validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label="Password: ", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
