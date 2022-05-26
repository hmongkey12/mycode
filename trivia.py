from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
@app.route("/landingpage")
def landingpage():
    return render_template("postmaker.html")

@app.route("/correct")
def correct():
    return "You got the correct Answer!"

@app.route("/handleanswer", methods=["POST"])
def login():
    if request.form.get("nm"):
        answer = request.form.get("nm")
        if(answer == "correct"):
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("landingpage"))
    else:
        print('hi')
        return redirect(url_for("landingpage"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

