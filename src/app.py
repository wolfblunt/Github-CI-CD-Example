from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Aman!"


if __name__ == "__main__":
    app.run()
