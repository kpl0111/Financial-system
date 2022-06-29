from unicodedata import category
from data_ind import *
from user_sys import *

class dbs:
    def __init__(self) -> None:
        self.stafflist, self.dbalist, self.cashierlist, self.managerlist = [], [], [], []
        self.read_users()

    def read_users(self):
        with open(dir_root+dir_staff, 'rw') as f:
            item = f.readline()
            tmp = staff()
            tmp.fromstr(item)
            self.stafflist.append(tmp)
        with open(dir_root+dir_DBA, 'rw') as f:
            item = f.readline()
            tmp = dba()
            tmp.fromstr(item)
            self.dbalist.append(dba)
        with open(dir_root+dir_cashier, 'rw') as f:
            item = f.readline()
            tmp = cashier()
            tmp.fromstr(item)
            self.cashierlist.append(item)
        with open(dir_root+dir_manager, 'rw') as f:
            item = f.readline()
            tmp = manager()
            tmp.fromstr(item)
            self.managerlist.append(item)
            
    def item_for_check(self, uid, type):
        if type == 'staff':
            for i in self.stafflist:
                if i.uid == uid:
                    return i
