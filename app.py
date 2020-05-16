import functools
import json
from flask import jsonify
import os

import flask

import google_auth

app = flask.Flask(__name__)
app.secret_key = 'FGR%^$VJ&(&super)UB^fgsecret%*Gr^key'

app.register_blueprint(google_auth.app)


@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return jsonify({'user_info': json.dumps(user_info, indent=4),'message':'You have logged in successfully'})

    return jsonify({'message':'You are not currently logged in.'})
from google_auth import logout
@app.route('/google/logout')
def signOutUser():
    logout()


if __name__ == '__main__':
    app.run(host="localhost", debug=True)
