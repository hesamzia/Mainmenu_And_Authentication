# Mainmennu-And-Authentication                                                             (LAST VERSION)      
Please read the author's introduction below...

# TO DO
- [X] Preparing the application template with Flask Blueprint
- [X] Finding a good example of menu and Authentication
- [X] Setting up new repository in GitHub
- [X] Create the application folder, create a virtual environment, and install Flask.
- [X] Preparing the application folder and opening it in VS Code
- [X] Creating menus with the help of example and preparing routes and the main structure of the program
- [X] Creating user models(database structure)
- [X] Configuring Database
- [X] Start connecting to the database by setting up a sign-up. 
- [X] Summarizing the init file and concentrating the source in other files
- [X] Add logout and protect profile and logout
- [X] Show home,login,signup if no one logged in and home,profile,logout if a person loggedin
- [ ] Make remember passwor in login
# Introduction
When I was programming in the past, one of the most important issues in any program was the main menus of the program and creating appropriate access to them for users. It was very difficult when using standard C or ANSI C , but later it became easier with the advent of Visual languages.That's why I thought I'd do this with Python and Flask, and have a standard menu that I could use in any program with a little modification.
In my new programming career, I'm trying to use artificial intelligence as an employee and collaborator. I planned to do this with the help of artificial intelligence and codeium (windsurf).
I didn't have a great experience with Codium when I started working on this project. I realized that AI doesn't have much memory for solving problems, and when you have serial problems, it forgets and doesn't consider previous problems, and sometimes it can get confused. I recommend that you don't give it large programs and try to lead the execution yourself and give it small to medium-sized functions to execute. Make sure the functions you give it are clearly defined with their inputs, outputs, and necessary conditions, and be sure to constantly remind it of these conditions during debugging.
Because of these AI problems, I took help from my dear Google and I will choose one of the existing examples and modify it according to my needs. Along the way, I will take help from Codium. I feel like this is the best way to program right now.
# About Application
In this application, we prepare a customizable menu  with a program to authenticate to it. This application can be the basis of other applications we will code. In this application, we will do:
* Use the Flask-Login library for session management.
* Use the built-in Flask utility for hashing passwords.
* Add protected pages to the app for logged in users only.
* Use Flask-SQLAlchemy to create a User model.
* Create sign-up and login forms for the users to create accounts and log in.
* Flash error messages back to users when something goes wrong.
* Use information from the user’s account to display on the profile page. 
* Use flask blueprint for making application components and supporting common patterns within an application or across applications.

# How to run app
- make a folder
- clone from github
- make venv
- Pip install –r requirmetns.txt 
- set FLASK_APP=Mainmennu-And-Authentication
- flask --app Mainmennu-And-Authentication run

