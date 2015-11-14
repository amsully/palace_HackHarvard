from flask import Flask, render_template
import os 
from flask.ext.pymongo import PyMongo



os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


app = Flask(__name__, tmpl_dir)
app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return  "What?"


@app.route("/createTopic")
def createTopic():
	print "IN HERE"
	return render_template("newTopic.html")


@app.route("/topic/<topic_title>", methods=["POST"])
def createTopicBackend():
	print "IN CREATING THE BACKEND" 


if __name__ == '__main__':
    app.run()