from flask import jsonify, make_response


users = []


class UserModel():
    """docstring for Orsersoperations"""

    def __init__(self):
        self.users = users

    def save(self, name, email, username, password):

        payload = {
            'id': len(self.users) + 1,
            'name': name,
            'email': email,
            'username': username,
            'password': password
        }

        self.users.append(payload)

        return self.users

    def checkifexist(self, username):

        for user in self.users:
            if(user['username'] == username):
                return True

    def login(self, username, password):

        for item in self.users:

            if (item['username'] == username):

                if item['password'] == password:

                    return make_response(jsonify(
                        {
                            'Message': "User signed in successfully"
                        }), 200)

            return make_response(jsonify(
                {
                    'Message': "Username and password does no match"
                }), 401)
