#!/usr/bin/python3
"""
modules to run a simple flask app with babel translation
"""
from flask import request, Flask, render_template
from flask_babel import Babel


class Config:
    """Set default language configuration for language . """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the locale for the current locale .

    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def school():
    """
    This function is used to render a school page .
    it is used for example in the example of the school module .

    """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(port="50070", host="0.0.0.0", debug=True)
