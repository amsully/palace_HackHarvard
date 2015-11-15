from flask import Flask, render_template, request, jsonify
import os 
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from mongoclient import client


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/templates')


app = Flask(__name__, tmpl_dir)
app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
mongo = PyMongo(app)



@app.route('/')
def home():
   #check if the user is logged in. 
   #starred homes. 
   #when you login, you encrypt your password. 

   return render_template("index.html")



def main(argv):
	global userID

@app.route("/createTopic")
def createTopic():
	print ("IN HERE")
	return render_template("newTopic.html")

@app.route("/createNode")
def createNode():
	print ("IN: Create Topic")
	return render_template("newNode.html")

#should be able to edit their nodes.

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

    	returned_info ={"current_title": parent_topic,  "connected_title": topic_name,   "connected_description": topic_description }
	#if the parent topic does not exist, create a new one. 
	#if there is a otpic. 
	if myCursor.count() > 1 : 

		#insert the uUID of the new topic into that parent topic. 
  		myCursor = db.find({'name':parent_topic })
    	topic = myCursor[0]
    	print topic
    	list_topics = topic['topic_branches'] #get the list of branches. 
    	print "TOPICS CONNECTED"
    	print list_topics 
    	list_topics.append(result) #should append to the topic. 
    	print topic  

   

    #you need: 
    #title of the current topic 
    #title of hte topic it's you created   
    #description 

	return  jsonify(returned_info)


@app.route("/api/user", methods=["POST"])
def createUser():
	print "IN THE USER API "
	name = request.form["name"]
	user_id= request.form["id"]
	global user_id
	userID = user_id
	print "USER ID"
	print userID
	if alreadyExists(user_id, "users") != True:
		client = MongoClient()
		db = client.users 
		user = db.user_id
		result = user.insert({ 'user_id' : user_id , 'name':name, 'liked_nodes': [], 'friends':[] })
		print result
	return "done!"



@app.route("/api/user_add_nodes", methods= ["POST"])
def addToUser():
	print "ADDING NODE OT USER" 
	video_id= request.form["id"]
	print userID  #check for lgobal variable. 
	myCursor = db.find({'name'  })
    	topic = myCursor[0]
    	print topic
    	list_topics = topic['liked_nodes'] #get the list of branches. 
    	print "LIKED NODES "
    	print list_topics 
    	list_topics.append(video_id) #should append to the topic. 
    	#append to liked videos. 
    	print topic  
    	return "done"





def alreadyExists(user_id, collection):
	client = MongoClient()
	db = client.users 
	print bool(db.user_id.find({"user_id": user_id}))
   	return bool(db.user_id.find({"user_id": user_id}))


	#The lfow ist that i need to save this into mongodb. 


@app.route("/graphics") 
def graphic():
	print "NEW"
	return render_template("graphics.html")

@app.route("/topic/newNode", methods=["POST"])
def createTopicNode():
	print ("IN CREATING NODE")
	print request

	
	node_link = request.get_json().get("node_link", "")
	node_description = request.get_json().get("node_description", "")
	node_rating = request.get_json().get("node_rating", "")
	
	db = client.topics
	topic = db.topic_name
	result = topic.insert({ 'node_description': node_description, 'rating': node_rating, 'connected_nodes': [], 'topic_branches': [] })
	print db
	return "done"


if __name__ == '__main__':
	

	db = client.topics.topic_name
	result = db.insert_one({ 'name': "Palace", 'description': "Start", 'rating': 10, 'connected_nodes': [], 'topic_branches': [] }).inserted_id
	app.run(host='0.0.0.0',port=80)






