from flask import Flask, render_template, request
import os 
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient



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
	print ("IN HERE")
	return render_template("newTopic.html")


@app.route("/topic/newTopic", methods=["POST"])
def createTopicBackend():
	print ("IN CREATING THE BACKEND")
	print request
	topic_name = request.get_json().get("topic_name", "")
	topic_description = request.get_json().get("topic_description", "")
	rating = request.get_json().get("rating", "")
	client = MongoClient()
	db = client.topics
	topic = db.topic_name
	result = topic.insert({ 'UUID': 12452523324, 'description': topic_description, 'rating': rating, 'connected_nodes': [], 'topic_branches': [] })
	print db
	return "done"



if __name__ == '__main__':
    app.run()