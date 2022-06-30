""" BaseModel class """

from datetime import datetime
import uuid


class BaseModel():
    """
    class that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = ???

    def save(self):
        """updates public attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
