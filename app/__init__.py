from flask import Flask

# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # db.init_app(app)

    return app
