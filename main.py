from flask import Flask, request, redirect, render_template

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_signup():
    return render_template('signup.html')

@app.route("/validation", methods=['POST'])
def validate():

@app.route("/welcome/?username=####")
def welcome():



app.run()

