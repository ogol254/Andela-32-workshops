from flask_restful import Resource
from flask import jsonify, make_response, request

# local
from ..models.user_models import UserModel


class Authentication(Resource, UserModel):
    """docstring for Authentication"""

    def __init__(self):
        self.user = UserModel()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if self.user.checkifexist(username) == True:

            result = self.user.login(username, password)

            return result

        return make_response(jsonify(
            {
                'Message': 'User does not exist'
            }), 401)


class UserRegistration(Resource, UserModel):
    """docstring for Orders"""

    def __init__(self):
        self.user = UserModel()

    def post(self):
        data = request.get_json()
        name = data['name']
        email = data['email']
        username = data['username']
        password = data['password']

        result = self.user.save(name, email, username, password)

        return make_response(jsonify(
            {
                'Message': 'Success',
                'status': 'ok',
                'Data': result
            }), 201)
