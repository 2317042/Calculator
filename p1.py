from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    # Directly returning HTML as frontend
    return """
    <html>
    <head><title>Calculator</title></head>
    <body>
        <h2>Simple Calculator</h2>
        <form action="/calculate" method="get">
            <input type="number" name="a" placeholder="Enter number a" required>
            <input type="number" name="b" placeholder="Enter number b" required>
            <select name="op">
                <option value="add">Add</option>
                <option value="sub">Subtract</option>
                <option value="mul">Multiply</option>
                <option value="div">Divide</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    """

@app.route("/calculate", methods=["GET"])
def calculate():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = request.args.get("op", "add")

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        result = "Error (division by zero)" if b == 0 else a / b
    else:
        result = "Invalid Operation"

    return f"<h3>Result: {result}</h3><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
