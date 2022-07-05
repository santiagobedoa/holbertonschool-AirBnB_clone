#!/usr/bin/python3
""" User class """

from models.base_model import BaseModel


class User(BaseModel):
    """
    class that represents a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize an User base on BaseModel """
        super().__init__(*args, **kwargs)
