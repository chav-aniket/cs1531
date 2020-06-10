'''
I HATE PYLINT
Lab05 Exercise 2
'''

from json import dumps
from flask import Flask, request

APP = Flask(__name__)

NAMES = []

@APP.route("/name/add", methods=['POST'])
def add_name():
    '''
    Adds a new name to the NAMES list
    '''
    data = request.get_json(force=True)
    NAMES.append(data['name'])
    return {}

@APP.route("/names", methods=['GET'])
def ret_names():
    '''
    Displays the NAMES list
    '''
    return dumps({
        'name':str(NAMES)
    })

@APP.route("/name/remove", methods=['DELETE'])
def rm_name():
    '''
    Removes a name from the NAMES list
    '''
    data = request.get_json()
    NAMES.remove(data['name'])
    return {}
    # try:
    #     NAMES.remove(data['name'])
    # except ValueError:
    #     return {"error":"Name does not exist"}
    # return {"error":"None"}

@APP.route("/name/reset", methods=['DELETE'])
def reset():
    '''
    Resets name list
    '''
    NAMES.clear()
    return {}

if __name__ == "__main__":
    APP.run(port=7117)
