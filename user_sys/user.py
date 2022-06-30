import string
# from DBserv import dbs

class user:
    def __init__(self, uid = 'empty', pwd = 'empty', utype = 'empty'):
        self.uid, self.pwd, self.utype = uid, pwd, utype
    
    def signup(self, uid : string, pwd : string, utype : string):
        pass

    def login(self, uid : string, pwd : string, tdbs, utype):
        checker = tdbs.item_for_check(uid, utype)
        if checker == None:
            return False
        if checker.uid == uid and checker.pwd == pwd:
            self.fromstr(checker.tostr())
            return True
        else:
            return False

    def reset_pwd(self, oldpwd : string, newpwd : string, tdbs):
        if oldpwd == self.pwd:
            self.pwd = newpwd
            tdbs.modify(self)
            tdbs.write_back()
            return True
        else:
            return False        

    def tostr(self):
        return str(self.uid) + ' ' + str(self.uid + self.pwd) + ' ' + str(self.utype)
    
    def fromstr(self, tstr):
        self.uid, self.pwd, self.utype = tstr.split()
        self.pwd = self.pwd[len(self.uid):]

    def __eq__(self, other):
        if type(other) == type(self):
            return self.tostr() == other.tostr()
        else:
            return False