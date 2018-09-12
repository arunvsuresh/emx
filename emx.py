from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def emx():

    if request.args.get("q") == "Email Address":
	    return "arunvsuresh@gmail.com"

    if request.args.get("q") == "Name":
        return "Arun Suresh"

    if request.args.get("q") == "Phone":
	return "4088216532"

    if request.args.get("q") == "Position":
	return "Software Engineer"

    if request.args.get("q") == "Years":
	return "3"

    if request.args.get("q") == "Referrer":
        return "LinkedIn"

    if request.args.get("q") == "Degree":
        return "University of California, Riverside - Bachelors in Science, Business Economics"

    if request.args.get("q") == "Resume":
	return ""
    if request.args.get("q") == "Source":
	return "https://github.com/arunvsuresh/emx"

    if request.args.get("q") == "Status":
        return "Yes"

    if request.args.get("q") == "Puzzle":
	request.args.get("q"), request.args.get("d")
    return "OK"


if __name__=='__main__':
    app.run(host='0.0.0.0')

