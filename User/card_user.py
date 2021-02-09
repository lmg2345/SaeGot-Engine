from . import user

class Card_User(user.User):
    _life = None
    def __init__(self, life, id = None, logon = False):
        super().__init__(id, logon)
        self._life = life

    def get_life(self, index=0):
        return self._life[index]

    def set_life(self, life, index=0):
        self._life = life[index]