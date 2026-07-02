import requests

class EmailConnector:

    def send(self, payload):

        response = requests.post(
            "http://127.0.0.1:5000/email",
            json=payload
        )

        return response.json()