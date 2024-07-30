#!/usr/bin/python3
from flask import request, Flask, render_template
from flask_babel import Babel


class Config:
    # ...
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object('1-app.Config')
# ...
babel = Babel(app, locale_selector=get_locale)
# ...


@app.route("/")
def school():
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
