from flask import Flask, render_template, request
import os 
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from mongoclient import client


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


#this links topic  to each other. 

@app.route("/topic/newTopic", methods=["POST"])
def createTopicBackend():
	#print ("IN CREATING THE BACKEND")
	#print request
	topic_name = request.get_json().get("topic_name", "")
	topic_description = request.get_json().get("topic_description", "")
	rating = request.get_json().get("rating", "")
	parent_topic = request.get_json().get("parent_topic", "")

	db = client.topics.topic_name
	result = db.insert_one({ 'name': topic_name, 'description': topic_description, 'rating': rating, 'connected_nodes': [], 'topic_branches': [] }).inserted_id
	#print result
	#print "FINDING THE PARENT NODE"
	myCursor =  db.find({'name':parent_topic}) 
	
	#if the parent topic does not exist, create a new one. 
	#if there is a otpic. 
	if myCursor.count() > 0 : 
		#insert the uUID of the new topic into that parent topic. 
  		myCursor = db.find({'name':parent_topic })
    	topic = myCursor[0]
    	print topic
    	list_topics = topic['topic_branches'] #get the list of branches. 
    	print "TOPICS CONNECTED"
    	print list_topics 
    	list_topics.append(result) #should append to the topic. 
    	print topic  


	return "done"



	#The lfow ist that i need to save this into mongodb. 




if __name__ == '__main__':
    app.run()






