from flask import Flask, request, jsonify

app = Flask(__name__)

stores = [
    {
        "name": "store1",
        "items":[
            {
                "name": "item1",
                "price": 125.5
            }
        ]
    }
]

@app.route('/')
def home():
    return "Hello world"


@app.route('/store')
def get_stores():
    return jsonify({"stores":stores})

app.run(port=5000)