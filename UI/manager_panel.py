import UI.log_panel
import tkinter as tk


def manager(tmd):
    window = tk.Tk()  # 创建窗口
    window.title("主管")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    t = tk.Entry(window, show=None)
    t.pack()
    t1 = tk.Entry(window, show=None)
    t1.pack()
    t2 = tk.Text(window, height=4)
    t2.pack()

    def modify_salary_base():
        num = float(t1.get())
        res = tmd.modify_salary_base(t.get(), num)
        t2.delete('1.0', 'end')
        if res:
            t2.insert('end', '修改成功')
        else:
            t2.insert('end', '修改失败')

    def settle_season():
        tmd.settle()
        t2.delete('1.0', 'end')
        t2.insert('end', '本季度薪资已结算')

    def get_report():
        tmp = tmd.analysis()
        t2.delete('1.0', 'end')
        t2.insert('end', tmp.printstr())

    def archive_season():
        tmd.archive_cur()
        t2.delete('1.0', 'end')
        t2.insert('end', '本季度已归档')

    def enroll_back():
        window.destroy()
        tmd.logout()
        UI.log_panel.log_panel(tmd)
        return

    def sec_exit():
        tmd.logout()
        window.quit()
    
    window.protocol('WM_DELETE_WINDOW', sec_exit)
    but0 = tk.Button(window, text="改变基础薪资", width=10, height=2, command=modify_salary_base)
    but0.pack()
    but1 = tk.Button(window, text="薪资季度结算", width=10, height=2, command=settle_season)
    but1.pack()
    but2 = tk.Button(window, text="报告", width=10, height=2, command=get_report)
    but2.pack()
    but3 = tk.Button(window, text="归档", width=10, height=2, command=archive_season)
    but3.pack()
    but4 = tk.Button(window, text="退出", width=10, height=2, command=enroll_back)
    but4.pack()
    #window.mainloop()  # 结束（不停循环刷新）