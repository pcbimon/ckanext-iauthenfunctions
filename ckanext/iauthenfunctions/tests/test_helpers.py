"""Tests for helpers.py."""

import ckanext.iauthenfunctions.helpers as helpers


def test_iauthenfunctions_hello():
    assert helpers.iauthenfunctions_hello() == "Hello, iauthenfunctions!"
