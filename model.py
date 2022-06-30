from DBserv import *
from table_sys import * 
from user_sys import *

class model:
    def __init__(self):
        self.usr = None
        self.db = dbs()

    def login(self, uid, pwd, utype):
        if utype == 'dba':
            self.usr = dba()
        elif utype == 'cashier':
            self.usr = cashier()
        elif utype == 'manager':
            self.usr = manager()
        else:
            self.usr = staff()
        return self.usr.login(uid, pwd, self.db)
    
    def logout(self):
        self.usr = None
        self.db.write_back()

    def commit_transaction(self, tid, mdf):
        assert type(self.usr) == cashier, 'user module type error\n' 
        tmp = self.usr.commit_transaction(tid, mdf)
        self.db.add_transaction(tmp)

    def query_salary(self):
        pass

    def analysis(self):
        pass
