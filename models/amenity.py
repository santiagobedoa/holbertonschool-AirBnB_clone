#!/usr/bin/python3
""" Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class that represents a amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Amenity base on BaseModel"""
        super().__init__(*args, **kwargs)
