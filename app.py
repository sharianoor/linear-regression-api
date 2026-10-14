from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Student registration number
REGISTRATION_NUMBER = "FA23-BDS-036"

# Student roll number used as the random seed
STUDENT_ROLL_NUMBER = 36

# Generate deterministic coefficients
random.seed(STUDENT_ROLL_NUMBER)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.route("/predict", methods=["GET"])
def predict():

    try:
        x1 = float(request.args.get("x1"))
        x2 = float(request.args.get("x2"))
        x3 = float(request.args.get("x3"))

        prediction = a1 * x1 + a2 * x2 + a3 * x3 + b

        return jsonify({
            "registration number": REGISTRATION_NUMBER,
            "prediction": round(prediction, 2)
        })

    except (TypeError, ValueError):

        return jsonify({
            "error": "Please provide valid x1, x2, and x3 values."
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
