from flask import Flask
#Webhook test
app = Flask(__name__)

@app.route("/")
def hello():
    return "OK"

app.run(host="0.0.0.0", port=5000)
