# Main Flask Application
from flask import Flask
# Import this to use the Jinja2 implemented in Flask modules
from flask import render_template
from flask import request

# Create the app
app = Flask(__name__)

# default method added is methods=['GET']
@app.route("/hello", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template("submit_page.html")
    elif request.method == 'POST':
        username = request.form["username"]
        return render_template("display_details.html", display_name=username)
    else:
        print("Error Check")    

if __name__== '__main__':
    app.debug = True
    app.run()