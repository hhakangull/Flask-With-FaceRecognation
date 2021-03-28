from flask import render_template, redirect, request, url_for, flash, session
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from Flask_App import db
from Flask_App.base import blueprint
from Flask_App.base.forms import LoginForm, CreateAccountForm
from Flask_App.base.models import User
from Flask_App.base.utils import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        # read form data
        username = form.username.data
        password = form.password.data
        # Locate user
        user = User.query.filter_by(username=username).first()
        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html', msg='Wrong user or password', form=form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm()
    session.pop('error', None)
    if request.method == "POST":
        user_TC = create_account_form.user_TC.data
        username = create_account_form.username.data
        firstname = create_account_form.firstname.data
        lastname = create_account_form.lastname.data
        email = create_account_form.email.data
        if len(create_account_form.password.data) < 6:
            flash('Parola Min 6 Karakterli olmalıdır.', 'warning')
            return redirect(url_for('base_blueprint.register'))
        # Check usename exists
        user = User.query.filter_by(user_TC=user_TC).first()
        if user:
            flash('TC No already registered', 'warning')
            return render_template('accounts/register.html',
                                   msg='TC NO already registered',
                                   success=False,
                                   form=create_account_form)

        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already registered', 'warning')
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered', 'warning')
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user

        user = User(**request.form)
        db.session.add(user)
        db.session.commit()
        flash('Kayıt Başarılı Oldu!', 'success')
        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form)
    else:
        return render_template('accounts/register.html', form=create_account_form)
