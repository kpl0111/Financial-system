from user_sys.FM import FM
from table_sys import tra_rec

class cashier(FM):
    def __init__(self) -> None:
        super().__init__()
    
    def commit_transaction(self, tid, mdf):
        return tra_rec(self.sid, tid, mdf)