import tkinter

top = tkinter.Tk()
top.wm_title("Feature Classes")

phones = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g']
buttons = []
frames = []

for i in phones:
    i = tkinter.Button(top, height=3, width=3, text=i)
    i.pack()

top.mainloop()
