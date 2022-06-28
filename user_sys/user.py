import string


class user:
    def __init__(self):
        self.uid, self.pwd, self.category = None, None, None
    
    def signup(self, uid : int, pwd : int, category : string):
        pass

    def login(self, uid : int, pwd : int):
        pass

    def reset_pwd(self, pwd : int):
        pass 