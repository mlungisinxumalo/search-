import os

from flask import Flask,  redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    # get input from user
    user_input = request.form.get("user_input")
    print(f"User input: {user_input}")  # Debugging line

    # replace users input space characters into +
    modified_input = user_input.replace(" ", "+")

    # take replaced users input into url
    google_search_url = f'https://www.google.com/search?tbm=isch&q={modified_input}'
    return redirect(google_search_url)

@app.route("/index1")
def index1():
    return render_template("index1.html")

@app.route("/index2")
def index2():
    return render_template("index2.html")

if __name__ == '__main__':
    app.run(debug=True)




    