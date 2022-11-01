from store import app
from flask import render_template
from store.models import Item
from store.forms import RegisterForm

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route('/store')
def store():
    items = Item.query.all()
    return render_template('store.html', items=items)


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)