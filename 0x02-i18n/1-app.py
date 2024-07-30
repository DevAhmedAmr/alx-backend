#!/usr/bin/python3
from flask import request, Flask, render_template
from flask_babel import Babel


class Config:
    # ...
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object('1-app.Config')
babel = Babel(app)


@app.route("/")
def school():
    """
    This function is used to render a school page .
    it is used for example in the example of the school module .

    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
