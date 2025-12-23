from flask import Flask

app = Flask(__name__)
@app.route("/")
def Index():
    index = 4 
    return "hello world test"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True, port = 5002)
