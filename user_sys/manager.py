from user_sys.FM import FM
from table_sys import *

class manager(FM):
    def __init__(self):
        super().__init__()

    def mdf_salary_base(self, sid, mdf, tdbs):
        for i, j in enumerate(tdbs.stafflist):
            print(j.sid, sid)
            if j.sid == sid:
                tdbs.stafflist[i].salary += mdf
                return True
        return False

    def settle_season(self, tdbs):
        salary_list = []
        for i, j in enumerate(tdbs.stafflist):
            salary_list.append(salary_table())
            salary_list[i].sid = j.sid
            salary_list[i].salary_base = j.salary
            salary_list[i].final = j.salary
        for i, j in enumerate(tdbs.salary_recs):
            for k in range(len(salary_list)):
                if salary_list[k].sid == j.sid:
                    if j.mdf > 0:
                        salary_list[k].bonus += j.mdf
                    else:
                        salary_list[k].docked += j.mdf
                    salary_list[k].final += j.mdf
                    break 
        return salary_list

    def get_report(self, tdbs, salary_list):
        tmp = financial_table()
        for i, j in enumerate(salary_list):
            tmp.total_salary += j.final
        for i, j in enumerate(tdbs.tra_recs):
            if j.mdf > 0:
                tmp.total_income += j.mdf
            else:
                tmp.other_outcome += j.mdf
        tmp.final_profit = tmp.total_income + tmp.other_outcome - tmp.total_salary
        return tmp

    def archive_season(self, tdbs):
        pass