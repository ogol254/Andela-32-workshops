from flask_restful import Resource
from flask import jsonify, make_response, request

# local
from models import Products


class ProductsViews(Resource, Products):
    """docstring for Orders"""

    def __init__(self):
        self.ops = Products()

    def get(self):
        orders = self.ops.getorders()

        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My Products': orders
            }), 200)

    def post(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        quantity = data['quantity']

        result = self.ops.save(name, price, quantity)

        return make_response(jsonify(
            {
                'Message': 'Success',
                'status': 'ok',
                'Payload': result
            }), 201)
