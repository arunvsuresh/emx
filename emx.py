from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def emx():
    return "OK"

@app.route("/fullname")
def fullname():
    return "Arun Suresh"

if __name__=='__main__':
    app.run(host='0.0.0.0')

