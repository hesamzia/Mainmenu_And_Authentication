from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..__main__ import db
from ..models import User
'''
 This is the auth blueprint for the application.
 It handles user authentication, including login, signup, and logout.
 '''
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    # code to validate and login user goes here
    return render_template('login.html')


@auth.route('/signup')
def signup():
    # code to validate and signup user goes here
    # This will render the signup page where users can create an account
     return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    print(email, name, password)

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
    
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    # code to logout user goes here
    # This will handle user logout logic, such as clearing session data
    return 'Logout'