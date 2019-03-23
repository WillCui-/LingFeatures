import tkinter
from tkinter import BOTH

screen = tkinter.Tk()
screen.wm_title("Feature Classes")

phones = {'p': (0, 0),
          'b': (1, 0),
          't': (6, 0),
          'd': (7, 0),
          'ʈ': (10, 0),
          'ɖ': (11, 0),
          'c': (12, 0),
          'ɟ': (13, 0),
          'k': (14, 0),
          'g': (15, 0),
          'q': (16, 0),
          'ɢ': (17, 0),
          'ʔ': (20, 0),
          'm': (1, 1),
          'ɱ': (3, 1),
          'n': (7, 1),
          'ɳ': (11, 1),
          'ɲ': (13, 1),
          'ŋ': (15, 1),
          'ɴ': (17, 1),
          'ʙ': (1, 2),
          'r': (7, 2),
          'ʀ': (17, 2),
          'ɾ': (7, 3),
          'ɽ': (11, 3),
          'ɸ': (0, 4),
          'β': (1, 4),
          'f': (2, 4),
          'v': (3, 4),
          'θ': (4, 4),
          'ð': (5, 4),
          's': (6, 4),
          'z': (7, 4),
          'ʃ': (8, 4),
          'ʒ': (9, 4),
          'ʂ': (10, 4),
          'ʐ': (11, 4),
          'ç': (12, 4),
          'ʝ': (13, 4),
          'x': (14, 4),
          'ɣ': (15, 4),
          'χ': (16, 4),
          'ʁ': (17, 4),
          'ħ': (18, 4),
          'ʕ': (19, 4),
          'h': (20, 4),
          'ɦ': (21, 4),
          'ɬ': (6, 5),
          'ɮ': (7, 5),
          'ʋ': (3, 6),
          'ɹ': (7, 6),
          'ɻ': (11, 6),
          'j': (13, 6),
          'ɰ': (15, 6),
          'l': (7, 7),
          'ɭ': (11, 7),
          'ʎ': (13, 7),
          'ʟ': (15, 7)}

buttons = []
frames = []

for i in range(len(phones)):
    text = list(phones.keys())[i]

    frame = tkinter.Frame(screen, width=30, height=30)
    button = tkinter.Button(frame, text=text)

    frames.append(frame)
    buttons.append(button)

    frame.propagate(False)
    frame.grid(row=phones[text][1], column=phones[text][0], sticky="nsew")
    button.pack(expand=True, fill=BOTH)

screen.mainloop()
