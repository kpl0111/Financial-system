from user_sys import *
from DBserv import *
from table_sys import *
from model import model

a = model()
a.login('admin', 'admin', 'dba')

a.register('cash cash1234 cashier cirspectacle', 'cashier')
# a.settle()

a.logout()

a.login('cash', '1234', 'cashier')

a.commit_transaction('34u20ej0ek202i3ek20e23', 568)

a.logout()
#b.add_account('cirspectacle cirspectacle1910611 staff 1910611 zhengyuan 21 0 0', 'staff', a)

#a.write_back()