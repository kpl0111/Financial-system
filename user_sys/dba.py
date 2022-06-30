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
        return tdbs.add(tmp)

    def reset_acc(self, uid, tag_usr, tdbs):
        if uid != tag_usr:
            return None
        tag_usr.pwd = 'passwd'
        return tag_usr

    def del_acc(self, uid, utype, tdbs):
        pass 