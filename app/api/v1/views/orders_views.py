afrom flask_restful import Resource
from flask import jsonify, make_response, request

# local
from models import OrdersOperations


class Orders(Resource, OrdersOperations):
    """docstring for Orders"""

    def __init__(self):
        self.ops = OrdersOperations()

    def get(self):
        orders = self.ops.getorders()

        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'My orders': orders
            }), 201)

    def post(self):
        data = request.get_json()
        item1 = data['item 1']
        item2 = data['item 2']
        price = data['price']

        result = self.ops.save(item1, item2, price)

        return make_response(jsonify(
            {
                'Message': 'Success',
                'status': 'ok',
                'Data': result
            }), 201)
