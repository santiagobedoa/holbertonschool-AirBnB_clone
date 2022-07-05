#!/usr/bin/python3
""" Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that represents a Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Review base on BaseModel"""
        super().__init__(self, *args, **kwargs)
