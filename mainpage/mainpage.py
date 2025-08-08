from flask import Blueprint, render_template
'''
 This is the main (mainpage) blueprint for the application.
 It handles the main page and profile page.
 '''
main = Blueprint('main', __name__)

@main.route('/')
def index():
    print('/')
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')
