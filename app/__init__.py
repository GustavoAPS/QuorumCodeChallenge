from flask import Flask
from app.routes.legislator_routes import legislator_bp
from app.routes.bill_routes import bill_bp


# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # db.init_app(app)

    app.register_blueprint(legislator_bp)
    app.register_blueprint(bill_bp)

    return app
