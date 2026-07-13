from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.json

    print("\n===== NEW FEEDBACK =====")
    print(data)

    return jsonify({
        "message": "Feedback received successfully!"
    })

if __name__ == "__main__":
    app.run(debug=True)