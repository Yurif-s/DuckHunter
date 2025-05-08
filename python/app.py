from flask import Flask
from flask_cors import CORS # type: ignore
from routes.search import search_bp
from flasgger import Swagger # type: ignore

app = Flask(__name__)
CORS(app)
Swagger(app)

app.register_blueprint(search_bp)

@app.route("/")
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)