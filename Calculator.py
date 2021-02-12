from tkinter import *

wind = Tk()
wind.title("Calculator")
wind.geometry("390x380+400+100")
wind.resizable(0, 0)
wind.config(bg="#9fa8da")


class Calc:
    def __init__(self, index, xx, yy):
        t = textButList[index]
        if t == "=":
            button = Button(wind, width=w, height=h, command=lambda: self.btn(t), bg=colors[index], text=t,
                    activebackground="#ec407a", relief="groove", bd=4, cursor="hand2", font="1" ).place(x=xx, y=yy)
        elif t == "C":
            button = Button(wind, width=w, height=h, command=lambda: self.btn(t), bg=colors[index], text=t,
                    activebackground="#ec407a", relief="groove", bd=4, cursor="hand2", font="1").place(x=xx, y=yy)
        elif t == "del":
            button = Button(wind, width=w, height=h, command=lambda: self.btn(t), bg=colors[index], text=t,
                    activebackground="#ec407a", relief="groove", bd=4, cursor="hand2", font="1").place(x=xx, y=yy)
        else:
            button = Button(wind, width=w, height=h, command=lambda: self.btn(t), bg=colors[index], text=t,
                    activebackground="#ec407a", relief="groove", bd=4, cursor="hand2", font="1").place(x=xx, y=yy)

    def btn(self, tool):
        global globtxt
        if tool == "=":
            try:
                globtxt = str(eval(globtxt))
            except:
                globtxt = "--- Invalid Input ---"
            string.set(globtxt)
            globtxt = ""
        elif tool == "C":
            string.set("")
            globtxt = ""
        elif tool == "del":
            globtxt = globtxt[:-1]
            string.set(globtxt)
        else:
            globtxt = globtxt + str(tool)
            string.set(globtxt)


globtxt, string, w, h, xPos, yPos, myIndex = "", StringVar(), 6, 3, 10, 75, 0
field = Label(wind, width=38, height=2, textvariable=string, bg="#fce4ec", font="1").place(x=20, y=15)
textButList, colors = ["1","4","7","(","2","5","8","0","3","6","9",")","+","-","*","/","C","=","del","."],\
                               ["#e0f7fa","#e0f7fa","#e0f7fa","#81d4fa","#e0f7fa","#e0f7fa","#e0f7fa","#e0f7fa",
                                "#e0f7fa","#e0f7fa","#e0f7fa","#81d4fa","#81d4fa","#81d4fa","#81d4fa","#81d4fa",
                                 "#4db6ac","#4db6ac","#4db6ac","#81d4fa"]
for x in range(5):
    for y in range(4):
        mine = Calc(myIndex, xPos, yPos)
        yPos += 75
        myIndex += 1
    yPos = 75
    xPos += 75

wind.mainloop()
