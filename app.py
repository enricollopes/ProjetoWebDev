from flask import Flask

app = Flask(__name__)

import marcial.routes

if __name__ == "__main__":
    app.run()