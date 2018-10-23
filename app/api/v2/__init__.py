from flask_restful import Api
from flask import Blueprint

from views import ProductsViews

version2 = Blueprint('api2', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(ProductsViews, '/products')
