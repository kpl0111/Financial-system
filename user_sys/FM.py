from user_sys.user import user

class FM(user):
    def __init__(self) -> None:
        super().__init__()
        self.sid = 'empty'

    def tostr(self):
        return self.uid + ' ' + self.uid+self.pwd + ' ' + self.utype + ' ' + self.sid

    def fromstr(self, tstr):
        self.uid, self.pwd, self.utype, self.sid = tstr.split()
        self.pwd = self.pwd[len(self.uid):]