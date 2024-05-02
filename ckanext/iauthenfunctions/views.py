from flask import Blueprint


iauthenfunctions = Blueprint(
    "iauthenfunctions", __name__)


def page():
    return "Hello, iauthenfunctions!"


iauthenfunctions.add_url_rule(
    "/iauthenfunctions/page", view_func=page)


def get_blueprints():
    return [iauthenfunctions]
