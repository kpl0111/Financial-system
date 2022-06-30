from user_sys.FM import FM
from table_sys import *

class cashier(FM):
    def __init__(self) -> None:
        super().__init__()
    
    def commit_transaction(self, tid, mdf):
        return tra_rec(self.sid, tid, mdf)

    def commit_salary_rec(self, sid, mdf=0, info='empty'):
        return salary_rec(sid, mdf, info)