from DBserv import *
from table_sys import * 
from user_sys import *

class model:
    def __init__(self):
        self.usr = None
        self.db = dbs()
        self.salary_list = self.db.read_salary_table()

    def login(self, uid, pwd, utype):
        if utype == 'dba':
            self.usr = dba()
        elif utype == 'cashier':
            self.usr = cashier()
        elif utype == 'manager':
            self.usr = manager()
        else:
            self.usr = staff()
        return self.usr.login(uid, pwd, self.db, utype)

    def tlogin(self, uid, pwd):
        self.usr = staff()
        if self.usr.login(uid, pwd, self.db, 'staff'):
            return True
        self.usr = dba()
        if self.usr.login(uid, pwd, self.db, 'dba'):
            return True
        self.usr = cashier()
        if self.usr.login(uid, pwd, self.db, 'cashier'):
            return True
        self.usr = manager()
        if self.usr.login(uid, pwd, self.db, 'manager'):
            return True
        else:
            return False

    def logout(self):
        self.usr = None
        self.db.write_back()

    def commit_transaction(self, tid, mdf):
        assert type(self.usr) == cashier, 'user module type error\n' 
        tmp = self.usr.commit_transaction(tid, mdf)
        return self.db.add_transaction(tmp)

    def settle(self):
        assert type(self.usr) == manager, 'user module type error\n' 
        self.salary_list = self.usr.settle_season(self.db)
        self.db.save_salary_table(self.salary_list)

    def query_salary(self):
        assert type(self.usr) == staff, 'user module type error\n' 
        if self.salary_list == None:
            return None
        else:
            return self.usr.get_salary_tb(self.salary_list)

    def analysis(self):
        assert type(self.usr) == manager, 'user module type error\n'
        return self.usr.get_report(self.db, self.salary_list)

    def archive_cur(self):
        assert type(self.usr) == manager, 'user module type error\n'
        self.db.tra_recs, self.db.salary_recs = [], []
        self.salary_list = []
        self.db.save_salary_table(self.salary_list)
        self.salary_list = None

    def register(self, tstr, utype):
        assert type(self.usr) == dba, 'user module type error\n'
        return self.usr.add_account(tstr, utype, self.db)

    def reset_acc(self, uid, utype):
        assert type(self.usr) == dba, 'user module type error\n'
        return self.usr.reset_acc(uid, utype, self.db)

    def reset_pwd(self, oldpwd, newpwd):
        return self.usr.reset_pwd(oldpwd, newpwd, self.db)

    def modify_salary_base(self, sid, mdf):
        assert type(self.usr) == manager, 'user module type error\n'
        return self.usr.mdf_salary_base(sid, mdf, self.db)