from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    num1 = float(data.get("num1", 0))
    num2 = float(data.get("num2", 0))
    operator = data.get("operator")

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return jsonify({"error": "Division by zero not allowed"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operator"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
