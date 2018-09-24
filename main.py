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
    email_space_error = ''


    # Addresses password length requirements.
    # I placed password conditionals 1st so username & email
    #  errors wouldn't reset password to empty and therefore also
    #  trigger password length error
    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
        password = ''
        re_enter = ''

    # Addresses invalid use of space character
    else:
        for char in password:
            if char == ' ':
                password_error = "Password must not contain spaces"          
                password = ''
                re_enter = '' 
                break               
    
    # Addresses mismatched password confirmation
    if password != re_enter:
        password_mismatch = "Passwords don't match"
        password = ''
        re_enter = ''   


    # Addresses username length requirements
    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
        username = ''
        password = ''
        re_enter = ''
    
    # Addresses invalid use of space character (placed in 'else' for efficiency)
    else:
        for char in username:
            if char == ' ':
                username_error = "No spaces allowed in username"
                username = ''
                password = ''
                re_enter = '' 
                break               


    # Addresses allowing no email entry in form
    if email == '':
        email = ''
        password = ''
        re_enter = '' 
    
    else:
        # Addresses email length requirements 
        if 3 > len(email) or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters"
            email = ''
            password = ''
            re_enter = ''

        else:
            # Addresses necessity of '@' and "." characters
            if "@" not in list(email) or "." not in list(email):
                email_error = "Email must contain '@' and '.' to be valid"
                email = ''
                password = ''
                re_enter = ''            
            # Addresses invalid use of space character
            for char in email:
                if char == ' ':
                    email_space_error = "Email must not contain spaces"     
                    email = ''
                    password = ''
                    re_enter = ''                         
                    break

    return render_template('signup.html',
        username_error=username_error,
        password_error=password_error, 
        mismatch_error=password_mismatch,
        email_error=email_error,
        email_space_error=email_space_error, 
        username=username, 
        password=password,
        password_match=re_enter, 
        email=email)

# @app.route("/welcome/?username=####")
# def welcome():
    


app.run()