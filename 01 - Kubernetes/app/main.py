import socket
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello from Python! (IP: {socket.gethostbyname(socket.gethostname())})"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
