# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from gemini_wrapper import GeminieWrapper
from pymongo import MongoClient
from bson.json_util import dumps
import json

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
uri = "mongodb://localhost:27017/"
connection_string = "mongodb+srv://cjadhav132:v4dD1vZKIq4v9rUx@cluster0.yp7xx8y.mongodb.net/"
db_name = "nik"
collection_name = "llm"
client = MongoClient(connection_string)
db = client[db_name]
collection = db[collection_name]
ai = GeminieWrapper()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.post('/get_query')
def get_query():
    input_message = request.json["data"]
    content = ai.getContent(input_message)
    return content


@app.get("/all_records")
def all_records():
    data = list(collection.find())
    return dumps(data)

@app.post("/find_data")
def find_data():
    input_message = request.json["data"]
    query = ai.getQuery(input_message)
    aggreate_function = json.loads(query)
    data = collection.aggregate(aggreate_function)
    return dumps(list(data))


# main driver function
if __name__ == '__main__':
    # app.config['MONGO_URI'] = uri

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
