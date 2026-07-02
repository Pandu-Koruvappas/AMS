from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

JSON_FILE = "emails.json"


@app.route("/")
def home():
    return "Email API Running"


@app.route("/email", methods=["POST"])
def receive_email():

    data = request.json

    print("\nEMAIL RECEIVED")
    print(data)

    # Create file if not exists
    if not os.path.exists(JSON_FILE):

        with open(JSON_FILE, "w") as f:
            json.dump([], f)

    # Read existing emails
    with open(JSON_FILE, "r") as f:
        emails = json.load(f)

    # Add new email
    emails.append(data)

    # Save back
    with open(JSON_FILE, "w") as f:
        json.dump(
            emails,
            f,
            indent=4
        )

    return jsonify({
        "status": "success"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )