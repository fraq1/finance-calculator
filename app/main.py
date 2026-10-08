from flask import Flask, jsonify, request

from app.calculator import calculate_balance


app = Flask(__name__)


@app.get("/")
def index():
    return {
        "application": "Personal Finance Calculator",
        "status": "running",
        "endpoint": "/balance?income=100000&expense=35000",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/balance")
def balance():
    income = float(request.args.get("income", 0))
    expense = float(request.args.get("expense", 0))

    result = calculate_balance([income], [expense])

    return jsonify(
        {
            "income": income,
            "expense": expense,
            "balance": result,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
