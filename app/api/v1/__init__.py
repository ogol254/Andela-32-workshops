from flask_restful import Api
from flask import Blueprint

from views.orders_views import Orders
from views.user_views import Authentication, UserRegistration

version1 = Blueprint('api1', __name__, url_prefix='/api/v1')

api = Api(version1)

api.add_resource(Orders, '/orders')
api.add_resource(Authentication, '/login')
api.add_resource(UserRegistration, '/signup')
