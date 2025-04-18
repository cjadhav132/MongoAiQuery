# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from gemini_wrapper import GeminieWrapper
from pymongo import MongoClient
from bson.json_util import dumps

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client['Nik']
collection = db['users']
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
    content = ai.getQuery(input_message)
    print(type(content))
    # data = collection.find(content)
    # print(data)

    return content


# main driver function
if __name__ == '__main__':
    app.config['MONGO_URI'] = uri

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
