from flask import Blueprint, render_template
from flask_login import login_required, current_user
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
@login_required        # Protect the profile page so only logged in users can access it. 
                       #Ensure the user is logged in to access the profile page
def profile():
    return render_template('profile.html', name=current_user.name)
