from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def emx():
    if request.args.get("Email Address"):
        return "arunvsuresh@gmail.com"

    if request.args.get("Name"):
        return "Arun Suresh"

    return "OK"

if __name__=='__main__':
    app.run(host='0.0.0.0')

