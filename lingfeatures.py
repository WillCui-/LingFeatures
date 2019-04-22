import Tkinter
from Tkinter import *

from LingFeatures import phones

screen = Tkinter.Tk()
screen.wm_title("Feature Classes")

buttons = []
frames = []

ipa_chart = Tkinter.Frame(screen, padx=20, pady=20)
ipa_chart.pack()

entry = Tkinter.Frame(screen)
entry.pack()

for i in range(len(phones)):
    button_text = list(phones.keys())[i]

    frame = Tkinter.Frame(ipa_chart, width=30, height=30, borderwidth=1, relief=RIDGE)
    frame.propagate(False)
    frame.grid(row=phones[button_text][0][1], column=phones[button_text][0][0], sticky="nsew")

    button = Tkinter.Button(frame, text=button_text, borderwidth=0, bg="#77DD77", activebackground="#575A61",
                            activeforeground="#D0DB97")
    button.pack(expand=True, fill=BOTH)

    frames.append(frame)
    buttons.append(button)

text = Tkinter.Text(entry)
text.pack()

screen.mainloop()


def find_similar(sounds):
    if len(sounds) == 0:
        return []

    output = phones[sounds[0]][1]

    for sound in sounds[1:]:
        output = [s for s in output if s in phones[sound][1]]

    return output

