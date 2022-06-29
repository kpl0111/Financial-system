import string

class user:
    def __init__(self, uid = 'empty', pwd = 'empty', utype = 'empty'):
        self.uid, self.pwd, self.utype = uid, pwd, utype
    
    def signup(self, uid : string, pwd : string, utype : string):
        pass

    def login(self, uid : string, pwd : string):
        pass

    def reset_pwd(self, pwd : string):
        pass 

    def tostr(self):
        return str(self.uid) + ' ' + str(self.uid + self.pwd) + ' ' + str(self.utype)
    
    def fromstr(self, tstr):
        self.uid, self.pwd, self.utype = tstr.split()
        self.pwd = self.pwd[len(self.uid):]

    def __eq__(self, other):
        return self.tostr() == other.tostr()