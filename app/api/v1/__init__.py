from flask_restful import Api
from flask import Blueprint

from views import Orders

version1 = Blueprint('api1', __name__, url_prefix='/api/v1')

api = Api(version1)

api.add_resource(Orders, '/orders')
