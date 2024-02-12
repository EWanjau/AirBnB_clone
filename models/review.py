#!/usr/bin/python3
"""
class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ review attribute """
    place_id = ""
    user_id = ""
    text = ""
