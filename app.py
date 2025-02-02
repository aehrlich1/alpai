from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Alp AI!'


if __name__ == '__main__':
    app.run()