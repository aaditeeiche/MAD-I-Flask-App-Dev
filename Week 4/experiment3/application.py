# Main Flask Application
from flask import Flask
# Import this to use the Jinja2 implemented in Flask modules
from flask import render_template

# Create the app
app = Flask(__name__)

# default method added is methods=['GET']
@app.route("/hello", methods=['GET', 'POST'])
def hello_world():
    return render_template("submit_page.html")

if __name__== '__main__':
    app.debug = True
    app.run()