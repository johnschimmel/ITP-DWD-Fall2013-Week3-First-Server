import os
from flask import Flask, request # Retrieve Flask, our framework
app = Flask(__name__)   # create our flask app

# this is our main page
@app.route("/")
def index():
    return """Hello World!<br/><br/>
    <a href='/page2'>Visit page #2</a><br>
    <a href='/form'>Visit form page</a>"""


# this is the 2nd route - can be access with /page2
@app.route("/page2")
def page2():
	return "<h2>Welcome to page 2</h2><p>This is just amazing!</p>"


# new route will accept both a GET and POST request from the client (web browser)
@app.route("/form", methods=["GET","POST"])
def simpleform():

	# Did the client make a POST request?
	if request.method == "POST":

		# get the form data submitted and store it in a variable
		user_name = request.form.get('user_name', 'Tim Berners-Lee')

		# return custom HTML using the user submitted data
		return "<html><body><h3>Hello %s! What an interesting name.</h3><br><a href='/form'>back to form</a></body><html>" % user_name

	else:

		# client made a GET request for '/form'
		# return a simple HTML form that POSTs to itself
		return """<html><body>
		<form action="/form" method="POST">
			What's your name? <input type="text" name="user_name" id="user_name"/>
			<input type="submit" value="submit it"/>
		</form>
		</body></html>"""

# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)