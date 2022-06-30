import string
from user_sys.user import user
from user_sys.cashier import cashier
from user_sys.manager import manager
from user_sys.staff import staff

class dba(user):
    def __init__(self):
        super().__init__()

    def add_account(self, nitem : string, utype, tdbs):
        if utype == 'dba':
            tmp = dba()
            tmp.fromstr(nitem)
        elif utype == 'cashier':
            tmp = cashier()
            tmp.fromstr(nitem)
        elif utype == 'manager':
            tmp = manager()
            tmp.fromstr(nitem)
        else:
            tmp = staff()
            tmp.fromstr(nitem)
        return tdbs.add(tmp, utype)

    def reset_acc(self, uid, utype, tdbs):
        if utype == 'dba':
            for i,j in enumerate(tdbs.dbalist):
                if j.uid == uid:
                    tdbs.dbalist[i].pwd = 'passwd'
                    return True
        elif utype == 'cashier':
            for i,j in enumerate(tdbs.cashierlist):
                if j.uid == uid:
                    tdbs.cashierlist[i].pwd = 'passwd'
                    return True
        elif utype == 'manager':
            for i,j in enumerate(tdbs.managerlist):
                if j.uid == uid:
                    tdbs.managerlist[i].pwd = 'passwd'
                    return True
        else:
            for i,j in enumerate(tdbs.stafflist):
                if j.uid == uid:
                    tdbs.stafflist[i].pwd = 'passwd'
                    return True
        return False

    def del_acc(self, uid, utype, tdbs):
        pass 