import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/v1/message")
def hello():
    return "Hello World!"


@app.route("/v1/fruits", methods=['GET'])
def getFruitsList():
    thislist = [
        {'id': 0,'name': 'Mango'},
        {'id':1,'name':'Pine'},
        {'id':2, 'name':'Apple'},
        {'id':3, 'name':'Guava'},
        {'id':4,'name':'orange'},
        {'id':5,'name':'kiwi'},
        {'id':6,'name':'melon'},
        {'id':7,'name':'mango'}
    ]
    return jsonify(thislist)


# get astronauts list
@app.route('/v1/astronauts')
def getListOfAstronauts():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    # print output of the number of people in space
    print(data['number'])
    return data


# Books API
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/v1/books', methods=['GET'])
def getSpecificBook():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No Book ID provided. Please Specify an ID"

    # Create an empty list for the results
    results = []

    # loop through the list of the result
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


# Run the app on specified host and port
if __name__ == '__main__':
    app.run(host="localhost", port=7000, debug=True)
