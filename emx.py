from flask import Flask
app = Flask(__name__)

@app.route("/")
def emx():
    return "OK"

@app.route("/fullname")
def fullname():
    return "Arun Suresh"

if __name__=='__main__':
    app.run(host='0.0.0.0')

