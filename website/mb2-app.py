from datetime import datetime
from flask import Flask, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f200c84ba483588ffa60a7c81dc18287'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":
    app.run(debug=True)
