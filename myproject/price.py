from flask import Flask, jsonify
from pymongo import MongoClient
import pprint

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')

@app.route('/symbols', methods=['GET'])
def get_symbols():
    db = client['mydatabase']
    collection = db['hendres']
    symbols = collection.find({}, {'_id': False})
    return jsonify(list(symbols))

if __name__ == '__main__':
    app.run()
