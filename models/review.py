#!/usr/bin/python3
""" Doc """


from models.base_model import BaseModel


class Review(BaseModel):
    place_id = None
    user_id = None
    text = ""
