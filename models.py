# models.py

from dataclasses import dataclass

@dataclass
class Person:
   first_name: str
   last_name: str


import codecs

class User:
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name

    def __setstate__(self, state):
        self.name = codecs.decode(state["name"], "rot13")