import UI.log_panel
import tkinter as tk


def cashier(tmd):
    # 用户操作界面
    window = tk.Tk()  # 创建窗口
    window.title("出纳")  # 窗口标题
    window.geometry('500x400')  # 窗口大小，小写字母x
    t = tk.Entry(window, show=None)
    t.pack()
    lbl = tk.Label(window, text='输入交易id')
    lbl.pack()
    t1 = tk.Entry(window, show=None)
    t1.pack()
    lbl1 = tk.Label(window, text='输入收入/支出')
    lbl1.pack()
    tt = tk.Text(window, height=4)
    tt.pack()

    # 窗口的label
    def commit_transaction():
        num = t1.get()
        num = float(num)
        res = tmd.commit_transaction(t.get(), num)
        tt.delete('1.0', 'end')
        if res:
            tt.insert('end', '交易确认成功')
        else:
            tt.insert('end', '交易确认失败')

    def enroll_back():
        window.destroy()
        tmd.logout()
        UI.log_panel.log_panel(tmd)
        return

    def sec_exit():
        tmd.logout()
        window.quit()
    
    window.protocol('WM_DELETE_WINDOW', sec_exit)
    but1 = tk.Button(window, text="凭证管理", width=10, height=2, command=commit_transaction)
    but1.pack()
    but2 = tk.Button(window, text="退出", width=10, height=2, command=enroll_back)
    but2.pack()
    #window.mainloop()  # 结束（不停循环刷新）