from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lon": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lon": -80.13},
    {"id": 3, "campus": "DC", "lat": 38.89, "lon": -77.01},
]

next_id = 4
@app.route("/")
def index():
    return """
    <h1>FIU Campuses API</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li>
        <a href="/api/health">api/health</a>
        </li>
        <li>
        <a href="/api/items">api/items</a>
        </li>
        <li>
        <a href="/api/items/1">api/items/1</a>
        </li>
        <li>
        <a href="/hello">hello</a>
        </li>
        <li>
        <a href="/data">data</a>
        </li>
    </ul>
    """

# REQUIRED ENDPOINT #1
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello! Welcome to my Flask Micro-API."
    }), 200

# REQUIRED ENDPOINT #2 (GET + POST)
@app.route("/data", methods=["GET", "POST"])
def data():
    global next_id

    if request.method == "GET":
        return jsonify(DATA), 200

    if request.method == "POST":
        new_item = request.get_json()

        new_item["id"] = next_id
        next_id += 1
        DATA.append(new_item)

        return jsonify({
            "message": "Item added successfully",
            "item": new_item
        }), 201

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/items")
def items():
    return jsonify(DATA), 200

@app.route("/api/items/<int:id>")
def item(id):
    for i in DATA:
        if i["id"] == id:
            return jsonify(i), 200
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
