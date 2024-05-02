"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.iauthenfunctions.logic import validators


def test_iauthenfunctions_reauired_with_valid_value():
    assert validators.iauthenfunctions_required("value") == "value"


def test_iauthenfunctions_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.iauthenfunctions_required(None)
