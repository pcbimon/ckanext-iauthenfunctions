"""Tests for views.py."""

import pytest

import ckanext.iauthenfunctions.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "iauthenfunctions")
@pytest.mark.usefixtures("with_plugins")
def test_iauthenfunctions_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("iauthenfunctions.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, iauthenfunctions!"
