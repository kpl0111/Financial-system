import string
import time

class tra_rec: # transaction record item
    def __init__(self, sid : string, tid : string, mdf : float):
        self.sid, self.tid, self.mdf = sid, tid, mdf
        self.commit_time = time.time()
    
    def tostr(self):
        return self.sid + ',' + self.tid + ',' + str(self.mdf) + ',' + self.commit_time
    
    def fromstr(self, tstr):
        self.sid, self.mdf, self.commit_time = tstr.split(',')
        self.mdf = float(self.mdf)