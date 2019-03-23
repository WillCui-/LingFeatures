import tkinter
from tkinter import BOTH

screen = tkinter.Tk()
screen.wm_title("Feature Classes")

phones = {'p': [(0, 0), [0, 11], [15, 16, 17, 20, 21, 22, 23, 24]],
          'b': [(1, 0), [0, 8, 11], [15, 16, 17, 20, 21, 22, 23, 24]],
          't': [(6, 0), [0, 14, 15], [20, 21, 22, 23, 24]],
          'd': [(7, 0), [0, 8, 14, 15], [20, 21, 22, 23, 24]],
          'ʈ': [(10, 0), [0, 14], [20, 21, 22, 23, 24]],
          'ɖ': [(11, 0), [0, 8, 14], [20, 21, 22, 23, 24]],
          'c': [(12, 0), [0, 14, 16, 19, 20, 22], [24]],
          'ɟ': [(13, 0), [0, 8, 14, 16, 19, 20, 22], [24]],
          'k': [(14, 0), [0, 19, 20], [15, 16, 17, 22, 23, 24]],
          'g': [(15, 0), [0, 8, 19, 20], [15, 16, 17, 22, 23, 24]],
          'q': [(16, 0), [0, 19, 23], [15, 16, 17, 24]],
          'ɢ': [(17, 0), [0, 8, 19, 23], [15, 16, 17, 24]],
          'ʔ': [(20, 0), [0, 10], [15, 16, 17, 20, 21, 22, 23, 24]],
          'm': [(1, 1), [0, 1, 7, 8, 11], [3, 15, 16, 17, 20, 21, 22, 23, 24]],
          'ɱ': [(3, 1), [0, 1, 7, 8, 11, 13], [3, 15, 16, 17, 20, 21, 22, 23, 24]],
          'n': [(7, 1), [0, 1, 7, 8, 14, 15], [3, 20, 21, 22, 23, 24]],
          'ɳ': [(11, 1), [0, 1, 7, 8, 14], [3, 20, 21, 22, 23, 24]],
          'ɲ': [(13, 1), [0, 1, 7, 8, 14, 16, 19, 20, 22], [3, 24]],
          'ŋ': [(15, 1), [0, 1, 7, 8, 19, 20], [3, 15, 16, 17, 22, 23, 24]],
          'ɴ': [(17, 1), [0, 1, 7, 8, 19, 23], [3, 15, 16, 17, 24]],
          'ʙ': [(1, 2), [0, 1, 2, 4, 6, 8, 11], [3, 15, 16, 17, 20, 21, 22, 23, 24]],
          'r': [(7, 2), [0, 1, 2, 4, 6, 8, 14, 15], [3, 20, 21, 22, 23, 24]],
          'ʀ': [(17, 2), [0, 1, 2, 4, 6, 8, 19, 23], [3, 15, 16, 17, 24]],
          'ɾ': [(7, 3), [0, 1, 2, 4, 5, 8, 14, 15], [3, 20, 21, 22, 23, 24]],
          'ɽ': [(11, 3), [0, 1, 2, 4, 5,  8, 14], [3, 20, 21, 22, 23, 24]],
          'ɸ': [(0, 4), [0, 2, 3, 11], [15, 16, 17, 20, 21, 22, 23, 24]],
          'β': [(1, 4), [0, 2, 3, 8, 11], [15, 16, 17, 20, 21, 22, 23, 24]],
          'f': [(2, 4), [0, 2, 3, 11, 13], [15, 16, 17, 20, 21, 22, 23, 24]],
          'v': [(3, 4), [0, 2, 3, 8, 11, 13], [15, 16, 17, 20, 21, 22, 23, 24]],
          'θ': [(4, 4), [0, 2, 3, 14, 15, 16], [20, 21, 22, 23, 24]],
          'ð': [(5, 4), [0, 2, 3, 8, 14, 15, 16], [20, 21, 22, 23, 24]],
          's': [(6, 4), [0, 2, 3, 14, 15, 17], [20, 21, 22, 23, 24]],
          'z': [(7, 4), [0, 2, 3, 8, 14, 15, 17], [20, 21, 22, 23, 24]],
          'ʃ': [(8, 4), [0, 2, 3, 14, 16, 17], [20, 21, 22, 23, 24]],
          'ʒ': [(9, 4), [0, 2, 3, 8, 14, 16, 17], [20, 21, 22, 23, 24]],
          'ʂ': [(10, 4), [0, 2, 3, 14, 17], [20, 21, 22, 23, 24]],
          'ʐ': [(11, 4), [0, 2, 3, 8, 14, 17], [20, 21, 22, 23, 24]],
          'ç': [(12, 4), [0, 2, 3, 14, 16, 19, 20, 22], [24]],
          'ʝ': [(13, 4), [0, 2, 3, 8, 14, 16, 19, 20, 22], [24]],
          'x': [(14, 4), [0, 2, 3, 19, 20], [15, 16, 17, 22, 23, 24]],
          'ɣ': [(15, 4), [0, 2, 3, 8, 19, 20], [15, 16, 17, 22, 23, 24]],
          'χ': [(16, 4), [0, 2, 3, 19, 23], [15, 16, 17, 24]],
          'ʁ': [(17, 4), [0, 2, 3, 8, 19, 23], [15, 16, 17, 24]],
          'ħ': [(18, 4), [0, 2, 3, 19, 21, 23], [15, 16, 17, 24]],
          'ʕ': [(19, 4), [0, 2, 8, 19, 21, 23], [15, 16, 17, 24]],
          'h': [(20, 4), [2, 3, 9], [15, 16, 17, 20, 21, 22, 23, 24]],
          'ɦ': [(21, 4), [2, 3, 8, 9], [15, 16, 17, 20, 21, 22, 23, 24]],
          'ɬ': [(6, 5), [0, 2, 3, 14, 15, 18], [20, 21, 22, 23, 24]],
          'ɮ': [(7, 5), [0, 2, 3, 8, 14, 15, 18], [20, 21, 22, 23, 24]],
          'ʋ': [(3, 6), [1, 2, 4, 8, 11, 13], [3, 15, 16, 17, 20, 21, 22, 23, 24]],
          'ɹ': [(7, 6), [1, 2, 4, 8, 14, 16], [3, 20, 21, 22, 23, 24]],
          'ɻ': [(11, 6), [0, 1, 2, 4, 8, 14], [3, 20, 21, 22, 23, 24]],
          'j': [(13, 6), [1, 2, 4, 8, 19, 20, 22, 24], [15, 16, 17]],
          'l': [(7, 7), [0, 1, 2, 4, 8, 14, 15, 18], [3, 20, 21, 22, 23, 24]],
          'ɭ': [(11, 7), [0, 1, 2, 4, 8, 14, 18], [3, 20, 21, 22, 23, 24]],
          'ʎ': [(13, 7), [0, 1, 2, 4, 8, 14, 16, 18, 19, 20, 22], [3,  24]],
          'ʟ': [(15, 7), [0, 1, 2, 4, 8, 19, 20], [15, 16, 17, 22, 23, 24]]}

buttons = []
frames = []

for i in range(len(phones)):
    text = list(phones.keys())[i]

    frame = tkinter.Frame(screen, width=30, height=30)
    button = tkinter.Button(frame, text=text)

    frames.append(frame)
    buttons.append(button)

    frame.propagate(False)
    frame.grid(row=phones[text][0][1], column=phones[text][0][0], sticky="nsew")
    button.pack(expand=True, fill=BOTH)

screen.mainloop()
