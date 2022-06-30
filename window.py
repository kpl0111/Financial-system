from UI import *
from UI.log_panel import log_panel
from user_sys import *
from table_sys import *
from model import model

class sys_ui:
    def __init__(self) -> None:
        self.sysmodel = model()
        log_panel(self.sysmodel)

if __name__ == '__main__':
    sys_ui()