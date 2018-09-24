from flask import Flask, request, redirect, render_template
import string


app= Flask(__name__)
app.config['DEBUG'] = True


# renders the signup page
@app.route("/signup")
def display_signup():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def validate():
    
    # Retrieves data entered into signup form
    username = request.form['username']
    password = request.form['pw']
    re_enter = request.form['re-enter']
    email = request.form['email']

    # Initializes error messages
    username_error = ''
    password_error = ''
    password_mismatch = ''
    email_error = ''

################ REMEMBER to inform the user of what they did wrong!!!!! ####################

    # Addresses username length requirements
    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"
        username = ''
        password = ''
        re_enter = ''
    
    # Addresses invalid use of space character (placed in 'else' for efficiency)
    else:
        for char in username:
            if char == ' ':
                username_error = "That's not a valid username"
                username = ''
                password = ''
                re_enter = '' 
                break               


    # Addresses password length requirements
    if len(password) < 3 or len(password) > 20 or " " in password.split():
        password_error = "That's not a valid password"
        password = ''
        re_enter = ''

    # Addresses invalid use of space character
    elif password_error == '':
        for char in password:
            if char == ' ':
                password_error = "That's not a valid password"          
                password = ''
                re_enter = '' 
                break               
    
    # Addresses mismatched password confirmation
    else:
        if password != re_enter:
            password_mismatch = "Passwords don't match"
            password = ''
            re_enter = ''   


    # Addresses allowing no email entry in form
    if email == '':
        email = ''
        password = ''
        re_enter = '' 
    
    # Addresses email length requirements & necessity of '@' and "." characters
    elif email != '':
        if 3 > len(email) or len(email) > 20 or "@" not in email.split() or "." not in email.split():
            email_error = "That's not a valid email"
            email = ''
            password = ''
            re_enter = ''

    # Addresses invalid use of space character
    else:
        for char in email:
            if char == ' ':
                email_error = "That's not a valid email"     
                password = ''
                re_enter = '' 
                break                        

    return render_template('signup.html',
        username_error=username_error,
        password_error=password_error, 
        mismatch_error=password_mismatch,
        email_error=email_error, 
        username=username, 
        password=password,
        password_match=re_enter, 
        email=email)

# @app.route("/welcome/?username=####")
# def welcome():
    


app.run()

########### NOTES ######################
# signup is accepting spaces. email is giving error message when it shouldn't. The culprit is likely in how I used the str.split()
#  method in the 'if' conditionals for all of those input fields