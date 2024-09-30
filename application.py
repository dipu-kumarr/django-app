# application.py
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World itsme '

if __name__ == "__main__":
    application.run()
