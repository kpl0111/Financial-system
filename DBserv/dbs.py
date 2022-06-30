import enum
import os
from DBserv.data_ind import *
from table_sys.salary_rec import salary_rec
from table_sys.salary_table import salary_table
from table_sys.tra_rec import tra_rec
from user_sys import *

class dbs:
    def __init__(self) -> None:
        self.stafflist, self.dbalist, self.cashierlist, self.managerlist = [], [], [], []
        self.tra_recs, self.salary_recs = [], []
        self.read_users()

    def read_users(self):
        if not os.path.exists(dir_root):
            os.mkdir(dir_root)
        with open(dir_root+dir_staff, 'a') as f:
            pass
        with open(dir_root+dir_DBA, 'a') as f:
            pass
        with open(dir_root+dir_cashier, 'a') as f:
            pass
        with open(dir_root+dir_manager, 'a') as f:
            pass
        with open(dir_root+dir_tra, 'a') as f:
            pass
        with open(dir_root+dir_sal, 'a') as f:
            pass

        with open(dir_root+dir_staff, 'r') as f:
            items = f.readlines()
            for item in items:
                tmp = staff()
                tmp.fromstr(item)
                self.stafflist.append(tmp)
        with open(dir_root+dir_DBA, 'r') as f:
            items = f.readlines()
            for item in items:
                tmp = dba()
                tmp.fromstr(item)
                self.dbalist.append(tmp)
        with open(dir_root+dir_cashier, 'r') as f:
            items = f.readlines()
            for item in items:
                tmp = cashier()
                tmp.fromstr(item)
                self.cashierlist.append(tmp)
        with open(dir_root+dir_manager, 'r') as f:
            items = f.readlines()
            for item in items:
                tmp = manager()
                tmp.fromstr(item)
                self.managerlist.append(tmp)
        with open(dir_root+dir_tra, 'r') as f:
            items = f.readlines()
            for item in items:
                tmp = tra_rec()
                tmp.fromstr(item)
                self.tra_recs.append(tmp)
        with open(dir_root+dir_sal, 'r') as f:
            items = f.readlines()
            for item in items:
                tmp = salary_rec()
                tmp.fromstr(item)
                self.salary_recs.append(tmp)
        if len(self.dbalist) == 0:
            tmp = dba()
            tmp.fromstr('admin adminadmin dba')
            self.dbalist.append(tmp)

    def item_for_check(self, uid, type):
        if type == 'staff':
            for i in self.stafflist:
                if i.uid == uid:
                    return i
        elif type == 'dba':
            for i in self.dbalist:
                if i.uid == uid:
                    return i
        elif type == 'cashier':
            for i in self.cashierlist:
                if i.uid == uid:
                    return i
        else:
            for i in self.managerlist:
                if i.uid == uid:
                    return i
        return None

    def write_back(self):
        if not os.path.exists(dir_root):
            os.mkdir(dir_root)
        with open(dir_root+dir_staff, 'w') as f:
            for i, j in enumerate(self.stafflist):
                f.write(j.tostr() + '\n')
        with open(dir_root+dir_DBA, 'w') as f:
            for i, j in enumerate(self.dbalist):
                f.write(j.tostr() + '\n')
        with open(dir_root+dir_cashier, 'w') as f:
            for i, j in enumerate(self.cashierlist):
                f.write(j.tostr() + '\n')
        with open(dir_root+dir_manager, 'w') as f:
            for i, j in enumerate(self.managerlist):
                f.write(j.tostr() + '\n')
        with open(dir_root+dir_tra, 'w') as f:
            for i, j in enumerate(self.tra_recs):
                f.write(j.tostr() + '\n')
        with open(dir_root+dir_sal, 'w') as f:
            for i, j in enumerate(self.salary_recs):
                f.write(j.tostr() + '\n')
        
    def add(self, usr, utype):
        if utype == 'staff':
            for i in self.stafflist:
                if i.uid == usr.uid or i.sid == usr.sid:
                    return False
            self.stafflist.append(usr)
            return True
        elif utype == 'dba':
            for i in self.dbalist:
                if i.uid == usr.uid:
                    return False
            self.dbalist.append(usr)
            return True
        elif utype == 'cashier':
            for i in self.cashierlist:
                if i.uid == usr.uid or i.sid == usr.sid:
                    return False
            self.cashierlist.append(usr)
            return True
        elif utype == 'manager':
            for i in self.managerlist:
                if i.uid == usr.uid or i.sid == usr.sid:
                    return False
            self.managerlist.append(usr)
            return True
        return False

    def modify(self, usr):
        if usr.utype == 'staff':
            for i in range(len(self.stafflist)):
                if self.stafflist[i].uid == usr.uid:
                    self.stafflist[i] = usr
                    return True
        elif usr.utype == 'dba':
            for i in range(len(self.dbalist)):
                if self.dbalist[i].uid == usr.uid:
                    self.dbalist[i] = usr
                    return True
        elif usr.utype == 'cashier':
            for i in range(len(self.cashierlist)):
                if self.cashierlist[i].uid == usr.uid:
                    self.cashierlist[i] = usr
                    return True
        else:
            for i in range(len(self.managerlist)):
                if self.managerlist[i].uid == usr.uid:
                    self.managerlist[i] = usr
                    return True
        return False

    def add_transaction(self, rec):
        for i in self.tra_recs:
            if i.tid == rec.tid:
                return False
        self.tra_recs.append(rec)
        return True

    def add_salary_m(self, rec):
        flag = False
        for i in self.salary_recs:
            if i.sid == rec.sid:
                flag = True
                break
        if flag: 
            self.salary_recs.append(rec)
        return flag

    def save_salary_table(self, salary_table):
        with open(dir_root + dir_sal_tlb, 'w') as f:
            for i in salary_table:
                f.write(i.tostr() + '\n')
    
    def read_salary_table(self):
        res = []
        if not os.path.exists(dir_root + dir_sal_tlb):
            return None
        with open(dir_root + dir_sal_tlb, 'r') as f:
            items = f.readlines()
            for i in items:
                tmp = salary_table()
                tmp.fromstr(i)
                res.append(tmp)
        if len(res) > 0:
            return res
        return None