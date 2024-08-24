from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
@app.route("/kush")
def kush():
    return "Hello Kushagra"
app.run(debug=True)
