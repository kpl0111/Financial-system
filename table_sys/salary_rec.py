class salary_rec:
    def __init__(self, sid = 'empty', mdf = 0, info = 'empty'):
        self.sid, self.mdf, self.info = sid, mdf, info

    def tostr(self):
        return self.sid + ',' + str(self.mdf) + ',' + self.info
    
    def fromstr(self, tstr):
        self.sid, self.mdf, self.info = tstr.split(',')
        self.mdf = float(self.mdf)