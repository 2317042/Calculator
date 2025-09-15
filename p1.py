from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator App is Running 🚀"

# Example calculator API
@app.route("/add", methods=["GET"])
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})

@app.route("/sub", methods=["GET"])
def sub():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a - b})

@app.route("/mul", methods=["GET"])
def mul():
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    return jsonify({"result": a * b})

@app.route("/div", methods=["GET"])
def div():
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    if b == 0:
        return jsonify({"error": "Division by zero not allowed"})
    return jsonify({"result": a / b})

if __name__ == "__main__":
    app.run(debug=True)

