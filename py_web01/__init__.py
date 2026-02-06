from flask import Flask

def create_app():
    app = Flask(__name__)
    from .views import acc
    app.register_blueprint(acc.ac)
    return app
    