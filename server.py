from flask import Flask, render_template, redirect, session, request
import random
app=Flask(__name__)
app.secret_key="im a secret"

@app.route("/")
def index():
    if "number" in session:
        pass
    else:
        session["number"]=random.randint(1,100)
    print(session["number"])
    return render_template("index.html")

@app.route("/guess",methods=["POST"])
def guess():
    print(request.form["guess"])
    if (int(request.form["guess"]))<session["number"]:
        session["answer"]="low"
    elif(int(request.form["guess"]))>session["number"]:
        session["answer"]="high"
    else :
        session["answer"]="correct"
    print(session["answer"])
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)