import string
import time

class tra_rec: # transaction record item
    def __init__(self, sid = 'empty', tid = 'null', mdf = 0):
        self.sid, self.tid, self.mdf = sid, tid, mdf
        self.commit_time = time.time()
    
    def tostr(self):
        return self.sid + ',' + self.tid + ',' + str(self.mdf) + ',' +str(self.commit_time)
    
    def fromstr(self, tstr):
        self.sid, self.tid, self.mdf, self.commit_time = tstr.split(',')
        self.mdf = float(self.mdf)
        self.commit_time = float(self.commit_time)