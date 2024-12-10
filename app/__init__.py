from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register the Blueprint
    from .routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app