import pygame

class User:
    _id = None
    _logon = False
    def __init__(self, id = None, logon = False):
        self._id = id
        self._logon = logon

    def login(self, id):
        self._id = id