"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from py_web01 import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=43210)