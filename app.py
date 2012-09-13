from flask import Flask # Retrieve Flask, our framework
app = Flask(__name__)   # create our flask app

# this is our main page
@app.route("/")
def index():
    return """Hello World!
    <br/><br/>
    <a href='/page2'>Visit page #2</a>"""


# this is the 2nd route - can be access with /page2
@app.route("/page2")
def page2():
	return "<h2>Welcome to page 2</h2><p>This is just amazing!</p>"


# start the webserver
if __name__ == "__main__":
	app.debug = True
	app.run()