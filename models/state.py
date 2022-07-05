#!/usr/bin/python3
""" State class """

from models.base_model import BaseModel


class State(BaseModel):
    """
    class that represents a state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a State base on BaseModel"""
        super().__init__(*args, **kwargs)
