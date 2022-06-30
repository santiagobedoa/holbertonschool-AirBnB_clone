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
        self.updated_at = datetime.now()

    def save(self):
        """Updates public attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = type(self).__name__
        for key, value in copy_dict.items():
            if isinstance(value, datetime):
                copy_dict[key] = value.isoformat()
        return copy_dict

    def __str__(self):
        """ String representation of an instance """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
