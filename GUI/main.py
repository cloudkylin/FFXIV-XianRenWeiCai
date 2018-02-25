import tkinter.ttk
import tkinter.messagebox
from tkinter import *
import ffcalculator

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.pos = [[]for i in range(9)]
        for i in range(9):
            self.pos[i] = IntVar()

        self.title("FFXIV-仙人微彩计算器")
        self.GUI()

    def GUI(self):
        window = Frame(self)
        window.pack()
        Label(window,text="从左上到右下").grid(row=0, column=0)
        Label(window, text="第一列").grid(row=0, column=1)
        Label(window, text="第二列").grid(row=0, column=2)
        Label(window, text="第三列").grid(row=0, column=3)
        Label(window, text="从右上到左下").grid(row=0, column=4)
        Label(window, text="第一行").grid(row=1, column=0)
        Label(window, text="第二行").grid(row=2, column=0)
        Label(window, text="第三行").grid(row=3, column=0)

        pos1combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[0],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=1, column=1)
        pos2combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[1],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=1, column=2)
        pos3combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[2],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=1, column=3)
        pos4combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[3],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=2, column=1)
        pos5combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[4],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=2, column=2)
        pos6combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[5],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=2, column=3)
        pos7combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[6],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=3, column=1)
        pos8combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[7],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=3, column=2)
        pos9combo = tkinter.ttk.Combobox(window, width=12, textvariable=self.pos[8],
                                         values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).grid(row=3, column=3)
        Button(window, width=12, text="OK", command=self.OK_Button).grid(row=1, column=4)
        Button(window, width=12, text="Reset", command=self.Reset_Button).grid(row=2, column=4)

    def OK_Button(self):
        x = []
        y = []
        for i in  range(9):
            num = self.pos[i].get()
            if num == 0:
                continue
            elif num > 9 or num < 0:
                tkinter.messagebox.showerror("输入错误", "位置 %d 的数字输错啦，快去看看是不是手抖啦？。" % (i+1))
                return
            elif num in y:
                tkinter.messagebox.showerror("输入重复", "位置 %d 的数字输重啦，快去看看是不是眼花啦？" % (i+1))
                return
            else:
                x.append(i)
                y.append(num)
        if len(x) != 4 or len(y) !=4:
            tkinter.messagebox.showerror("超过限制", "你好像没开对格子，要开好4个再来找窝哟~多开少开都不行哟~")
        cal = ffcalculator.analysis(x,y)
        msg = cal.bestline()
        tkinter.messagebox._show("提交成功", msg)

    def Reset_Button(self):
        for i in range(9):
            self.pos[i].set(0)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()