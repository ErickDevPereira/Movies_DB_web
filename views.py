from main import app
from flask import render_template, redirect, url_for, session, flash, get_flashed_messages
from forms import *
import db.conn as conn
import db.DML as dml
import db.DQL as dql
import utils.extraUtils as utils

@app.route('/sucess')
def success():
    return render_template('success.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    msgs = get_flashed_messages()
    form = LoginForm()
    if form.validate_on_submit():
        DB = conn.my_connection()
        if dql.validate_user(DB, form.username.data, utils.cryptograph_msg(form.password.data)):
            DB.close()
            pass #To be codded
        else:
            flash("This user doesn't exist or the password is wrong!")
            DB.close()
            return redirect(url_for('login'))
    fields = [form.username.errors, form.password.errors]
    return render_template('login.html', form = form, fields = fields, msgs = msgs)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    msgs = get_flashed_messages()
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        phone = form.phone.data
        email = form.email.data
        DB = conn.my_connection()
        if not dql.check_if_user_exists(DB, username):
            session['username'] = username
            session['email'] = email
            session['phone'] = phone
            dml.load_user(DB, username = username, password = utils.cryptograph_msg(password), email = email, phone = phone)
            DB.close()
        else:
            flash('This username has been used for someone')
            DB.close()
            return redirect(url_for('register'))
        return redirect(url_for('success'))
    fields = [form.username.errors, form.password.errors, form.conf_password.errors, form.email.errors, form.phone.errors]
    return render_template('register.html', form = form, fields = fields, msgs = msgs)