from flask import Flask, redirect, url_for
from routes.__init__ import blueprintA, blueprintB

app = Flask(__name__)
app.register_blueprint(blueprintA)
app.register_blueprint(blueprintB)


if __name__ == '__main__':
    app.run(debug=True)
