#!/usr/bin/python3
"""Defines lookup function an object attribute."""


def lookup(obj):
    """Return a list of object's available attribute."""
    return (dir(obj))
