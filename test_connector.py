from connector import EmailConnector

payload = {
    "subject": "Employee Details",
    "sender": "pandu22ds@gmail.com",
    "body": "Employee ID:1001"
}

connector = EmailConnector()

result = connector.send(payload)

print(result)
