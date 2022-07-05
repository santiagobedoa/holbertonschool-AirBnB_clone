#!/usr/bin/python3
""" City class """

from models.base_model import BaseModel


class City(BaseModel):
    """
    class that represents a city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a City base on BaseModel"""
        super().__init__(*args, **kwargs)
