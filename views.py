from run import app,limiter
from flask import jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask_restful import Resource

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/files', methods=['GET'])
@limiter.limit("100/day;10/hour;3/minute")
@jwt_required
def new_file():

    return jsonify({'answer': 42})
