# main imports, flask for our framework, jsonify for return jsons, request for reading the request from clients
from flask import Flask, jsonify, request

# execure Flask passing __name__ as a parameter
app = Flask(__name__)

# from superheroes import superheroes # this import a .py file with the json data

# Import the json file with the superheroes data
import json 

# read json file with open function
file = open('superheroes.json')

# load the json data from file with json.load function
jsonFromFile = json.load(file)

# extract the array of super heroes from the json (json.superheroes)
superheroes = jsonFromFile['superheroes']

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/superheroes')
def getSuperheroes():
    return jsonify({'superheroes': superheroes})

@app.route('/superheroes/<string:name>')
def getSuperheroe(name):
    response = [superheroe for superheroe in superheroes if superheroe['name'].lower().strip() == name.lower().strip()]
    # lower() = lowerCase ; strip() = trim
    if (len(response) > 0):
        return jsonify({'superheroe': response[0]})
    return jsonify({'message': 'Superheroe Not found'})

# Create Data Routes
@app.route('/superheroes', methods=['POST'])
def addSuperheroe():
    newSuperheroe = {
        'name': request.json['name'],
        'alias': request.json['alias'],
        'id': len(superheroes) + 1
    }
    superheroes.append(newSuperheroe)
    return jsonify({'superheroes': superheroes})

# Update Data Route
@app.route('/superheroes/<string:name>', methods=['PUT'])
def editSuperheroe(name):
    response = [superheroe for superheroe in superheroes if superheroe['name'].lower().strip() == name.lower().strip()]
    # lower() = lowerCase ; strip() = trim
    if (len(response) > 0):
        response[0]['name'] = request.json['name']
        response[0]['alias'] = request.json['alias']
        return jsonify({
            'message': 'Superheroe Updated',
            'superheroe': response[0]
        })
    return jsonify({'message': 'Superheroe Not found'})

# DELETE Data Route
@app.route('/superheroes/<string:name>', methods=['DELETE'])
def deleteSuperheroe(name):
    response = [superheroe for superheroe in superheroes if superheroe['name'].lower().strip() == name.lower().strip()]
    # lower() = lowerCase ; strip() = trim
    if len(response) > 0:
        superheroes.remove(response[0])
        return jsonify({
            'message': 'Superheroe Deleted',
            'superheroes': superheroes
        })