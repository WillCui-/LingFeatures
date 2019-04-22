import Tkinter
from Tkinter import *

from LingFeatures import phones
from LingFeatures import classes

from functools import partial


# Finds the features common in the sounds
def find_feature(sounds):
    if len(sounds) == 0:
        return []

    output = phones[sounds[0]][1]

    for sound in sounds[1:]:
        output = [s for s in output if s in phones[sound][1]]

    return output


# Finds sounds containing the features
def find_sounds(features):
    output = []

    if len(features) == 0:
        return []

    for feature in features:
        if feature not in classes:
            raise Exception("Feature {} does not exist".format(feature))

    for phone in phones.keys():
        if all(classes.index(feature) in phones[phone][1] for feature in features):
            output.append(phone)

    return output


class Main:
    def __init__(self, screen):
        self.screen = screen  # create the window
        self.screen.wm_title("Feature Classes")

        self.buttons = []
        self.frames = []

        self.selected_phones = []

        self.selected_features = []

        self.ipa_chart = Tkinter.Frame(self.screen, padx=20, pady=20)  # create the frame for the IPA
        self.ipa_chart.pack()

        self.feature_chart = Tkinter.Frame(self.screen, padx=20, pady=20)
        self.feature_chart.pack()

        self.entry = Tkinter.Frame(self.screen)
        self.entry.pack(fill=X)

        self.phone_entry = Tkinter.Frame(self.entry)  # create the frame for the phones
        self.phone_entry.pack(side=LEFT, expand=True)
        self.button_frame = Tkinter.Frame(self.entry)  # create the frame for the clear button
        self.button_frame.pack(side=LEFT, expand=True)
        self.feature_entry = Tkinter.Frame(self.entry)  # create the frame for the features
        self.feature_entry.pack(side=RIGHT, expand=True)

        self.out_frame = Tkinter.Frame(self.screen)  # create the frame for the output data
        self.out_frame.pack()

        for i in range(len(phones)):
            button_text = list(phones.keys())[i]

            frame = Tkinter.Frame(self.ipa_chart, width=30, height=30, borderwidth=1, relief=RIDGE)
            frame.propagate(False)
            frame.grid(row=phones[button_text][0][1], column=phones[button_text][0][0], sticky="nsew")

            button = Tkinter.Button(frame, text=button_text, borderwidth=0, bg="#77DD77", activebackground="#575A61",
                                    activeforeground="#D0DB97", command=partial(self.add_phone, button_text))
            button.pack(expand=True, fill=BOTH)

            self.frames.append(frame)
            self.buttons.append(button)

        for feature in classes:
            frame = Tkinter.Frame(self.feature_chart, relief=RIDGE, borderwidth=1)
            frame.pack(expand=True, fill=BOTH, side=LEFT)
            button = Tkinter.Button(frame, text=feature, borderwidth=0, bg="#77DD77", activebackground="#575A61",
                                    activeforeground="#D0DB97", command=partial(self.add_feature, feature))
            button.pack(expand=True, fill=BOTH, side=LEFT)

        self.phone_text = Tkinter.Label(self.phone_entry)
        self.phone_text.config(text="Selected Phones: \n")
        self.phone_text.pack(side=LEFT)

        self.phone_frame = Tkinter.Frame(self.button_frame, relief=RIDGE, borderwidth=1)
        self.phone_frame.pack(side=LEFT)
        self.phone_button = Tkinter.Button(self.phone_frame, text="Calculate features", borderwidth=0, bg="#77DD77",
                                           activebackground="#575A61", activeforeground="#D0DB97",
                                           command=self.display_phone)
        self.phone_button.pack()

        self.clear_frame = Tkinter.Frame(self.button_frame, relief=RIDGE, borderwidth=1)
        self.clear_frame.pack(side=LEFT)
        self.clear_button = Tkinter.Button(self.clear_frame, text="Clear", borderwidth=0, bg="#77DD77",
                                           activebackground="#575A61",
                                           activeforeground="#D0DB97", command=self.clear)
        self.clear_button.pack(expand=True, fill=Y, side=LEFT)

        self.feature_frame = Tkinter.Frame(self.button_frame, relief=RIDGE, borderwidth=1)
        self.feature_frame.pack(side=LEFT)
        self.feature_button = Tkinter.Button(self.feature_frame, text="Calculate phones", borderwidth=0, bg="#77DD77",
                                             activebackground="#575A61", activeforeground="#D0DB97",
                                             command=self.display_feature)
        self.feature_button.pack()

        self.feature_text = Tkinter.Label(self.feature_entry)
        self.feature_text.config(text="Selected Features: \n")
        self.feature_text.pack(side=LEFT)

        self.output_text = Tkinter.Label(self.out_frame)
        self.output_text.pack()

    def add_phone(self, phone):
        if phone not in self.selected_phones:
            self.selected_phones.append(phone)
        self.phone_text.config(text="Selected Phones: \n{}".format(" ".join(self.selected_phones)))

    def add_feature(self, feature):
        if feature not in self.selected_features:
            self.selected_features.append(feature)
        self.feature_text.config(text="Selected Features: \n{}".format(", ".join(self.selected_features)))

    def clear(self):
        self.selected_phones = []
        self.selected_features = []
        self.phone_text.config(text="Selected Phones: \n{}".format(" ".join(self.selected_phones)))
        self.feature_text.config(text="Selected Features: \n{}".format(", ".join(self.selected_features)))
        self.output_text.config(text="")

    def display_phone(self):
        output = find_feature(self.selected_phones)
        output = [classes[i] for i in output]
        if len(output) == 0:
            self.output_text.config(text="no similar features")
        else:
            self.output_text.config(text="[+{}]".format(", +".join(output)))

    def display_feature(self):
        output = find_sounds(self.selected_features)
        if len(output) == 0:
            self.output_text.config(text="no phones")
        else:
            self.output_text.config(text="/{}/".format("/ /".join(output)))


root = Tk()
my_main = Main(root)
root.mainloop()
