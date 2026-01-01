from main import app
from flask import render_template, redirect, url_for, session
from forms import *

@app.route('/sucess')
def success():
    return render_template('success.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    fields = [form.username.errors, form.password.errors]
    return render_template('login.html', form = form, fields = fields)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['email'] = form.email.data
        session['phone'] = form.phone.data
        return redirect(url_for('success'))
    fields = [form.username.errors, form.password.errors, form.conf_password.errors, form.email.errors, form.phone.errors]
    return render_template('register.html', form = form, fields = fields)