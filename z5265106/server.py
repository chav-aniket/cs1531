'''
A flask server for the backend of the 'helpr' application.

GET routes are passed arguments as URL parameters. POST and DELETE routes are
passed arguments as JSON data in the body of the request. All routes return data
as JSON.
'''

from flask import Flask, request

from werkzeug.exceptions import BadRequest

from json import dumps

import config
import helpr

APP = Flask(__name__)

@APP.route('/make_request', methods=['POST'])
def make_request():
    '''
    A route for helpr.make_request()

    Params: {"zid", "description"}

    Raises: BadRequest if helpr.make_request() raises a KeyError or ValueError.

    Returns: {}
    '''
    data = request.get_json()
    try:
        helpr.make_request(data['zid'], data['description'])
    except KeyError as err:
        raise BadRequest(err)

@APP.route('/queue', methods=['GET'])
def queue():
    '''
    A route for helpr.queue()

    Returns: A list in the same format as helpr.queue()
    '''
    return dumps(helpr.queue())

@APP.route('/remaining', methods=['GET'])
def remaining():
    '''
    A route for helpr.remaining()

    Params: ("zid")

    Raises: BadRequest if helpr.remaining() raises a KeyError.

    Returns: { 'remaining': n } where n is an integer
    '''
    zid = request.args.get('zid')
    try:
        n = helpr.remaining(zid)
    except KeyError as err:
        raise BadRequest(err)
    return dumps({
        'remaining': n
    })

@APP.route('/help', methods=['POST'])
def help():
    '''
    A route for helpr.help()

    Params: {"zid"}

    Raises: BadRequest if helpr.help() raises a KeyError.

    Returns: {}
    '''
    zid = request.get_json()['zid']
    try:
        helpr.help(zid)
    except KeyError as err:
        raise BadRequest(err)
    return dumps({})

@APP.route('/resolve', methods=['DELETE'])
def resolve():
    '''
    A route for helpr.resolve()

    Params: {"zid"}

    Raises: BadRequest if helpr.resolve() raises a KeyError.

    Returns: {}
    '''
    zid = request.get_json()['zid']
    try:
        helpr.resolve(zid)
    except KeyError as err:
        raise BadRequest(err)
    return dumps({})

@APP.route('/cancel', methods=['DELETE'])
def cancel():
    '''
    A route for helpr.cancel()

    Params: {"zid"}

    Raises: BadRequest if helpr.cancel() raises a KeyError.

    Returns: {}
    '''
    zid = request.get_json()['zid']
    try:
        helpr.cancel(zid)
    except KeyError as err:
        raise BadRequest(err)
    return dumps({})

@APP.route('/revert', methods=['POST'])
def revert():
    '''
    A route for helpr.revert()

    Params: {"zid"}

    Raises: BadRequest if helpr.revert() raises a KeyError.

    Returns: {}
    '''
    zid = request.get_json()['zid']
    try:
        helpr.revert(zid)
    except KeyError as err:
        raise BadRequest(err)
    return dumps({})

@APP.route('/reprioritise', methods=['POST'])
def reprioritise():
    '''
    A route for helpr.reprioritise()

    Returns: {}
    '''
    helpr.reprioritise()
    return dumps({})

@APP.route('/end', methods=['DELETE'])
def end():
    '''
    A route for helpr.end()

    Returns: {}
    '''
    helpr.end()
    return dumps({})

if __name__ == "__main__":
    # Do NOT change the port below. If you need to change the port number do so
    # by changing the value in config.py
    APP.run(port=config.PORT, debug=True)