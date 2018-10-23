from flask import Flask, Blueprint


from instance.config import app_config
from db_con import create_tables


def create_app():
    app = Flask(__name__)
    create_tables()

    from .api.v1 import version1 as v1
    app.register_blueprint(v1)

    from .api.v2 import version2 as v2
    app.register_blueprint(v2)

    return app
