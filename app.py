from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["NuevaTienda"]
collection = db["productos"]

@app.route('/productos', methods=['GET'])
def get_productos():
    productos = list(collection.find({},{"_id": 0}))
    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True)