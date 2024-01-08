from app import app
from flask_cors import CORS
from flask import Flask

CORS(app)

if __name__ == "__main__":
    app.run(port=8080, debug=False)