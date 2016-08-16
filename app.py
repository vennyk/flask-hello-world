#--		flask hello world --#

# import the flask class from the flask module
from flask import Flask

#create the application object
app = Flask(__name__)

# debug option

app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route('/hello')

#define the view using a function, which returns a string
def hello_world():
	return 'hello world'


# dynamic route
@app.route("/test/<search_query>")

def search(search_query):
	return search_query

@app.route("/<int:value>")
def int_type(value):
	print value+1
	return 'correct'

@app.route("/float/<float:value>")
def float_type(value):
	print value+1
	return 'correct'
@app.route("/path/<path:value>")
#dynamic route that accepts slashes
def path_type(value):
	print value
	return 'correct'

# dynamic route with explicit status code
@app.route("/name/<name>")
def index(name):
	if name.lower() == 'michael' :
		return "hello, {}".format(name)
	else :
		return "not found", 404

# start the developmnt server using the run() method
if __name__ == '__main__':
	app.run()