# coding=utf-8
import tkinter as tk
from tkinter import *

from functools import partial


class Main:
    def __init__(self, screen):
        self.ordered_phones = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʔ', 'm', 'ɱ', 'n', 'ɳ', 'ɲ',
                               'ŋ', 'ɴ', 'ʙ', 'r', 'ʀ', 'ɾ', 'ɽ', 'ɸ', 'β', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'ʂ',
                               'ʐ', 'ç', 'ʝ', 'x', 'ɣ', 'χ', 'ʁ', 'ħ', 'ʕ', 'h', 'ɦ', 'p͡f', 't͡ɬ', 't͡s', 'd͡z', 't͡ʃ',
                               'd͡ʒ', 'k͡x', 'ɬ', 'ɮ', 'ʋ', 'ɹ', 'ɻ', 'j', 'l', 'ɭ', 'ʎ', 'ʟ', 'i', 'y', 'ɨ', 'ʉ', 'ɯ',
                               'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'ɛ', 'œ', 'ə', 'ɞ', 'ʌ', 'ɔ', 'æ', 'a',
                               'ɶ', 'ɑ', 'ɒ', 'w', 'ʍ', 'ɥ', 'ɕ', 'ʑ', 't͡ɕ', 'd͡ʑ']

        # in format (x, y), [+ locations], [0 locations]
        self.phones = {'p': [(0, 0), [0, 11], [15, 16, 17, 20, 21, 22, 23, 24]],
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
                       'ɽ': [(11, 3), [0, 1, 2, 4, 5, 8, 14], [3, 20, 21, 22, 23, 24]],
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
                       'p͡f': [(2, 5), [0, 3, 11, 13], [15, 16, 17, 20, 21, 22, 23, 24]],
                       't͡ɬ': [(5, 5), [0, 3, 14, 15, 18], [20, 21, 22, 23, 24]],
                       't͡s': [(6, 5), [0, 3, 14, 15, 17], [20, 21, 22, 23, 24]],
                       'd͡z': [(7, 5), [0, 3, 8, 14, 15, 17], [20, 21, 22, 23, 24]],
                       't͡ʃ': [(8, 5), [0, 3, 14, 16, 17], [20, 21, 22, 23, 24]],
                       'd͡ʒ': [(9, 5), [0, 3, 8, 14, 16, 17], [20, 21, 22, 23, 24]],
                       'k͡x': [(14, 5), [0, 3, 19, 20], [15, 16, 17, 22, 23, 24]],
                       'ɬ': [(6, 6), [0, 2, 3, 14, 15, 18], [20, 21, 22, 23, 24]],
                       'ɮ': [(7, 6), [0, 2, 3, 8, 14, 15, 18], [20, 21, 22, 23, 24]],
                       'ʋ': [(3, 7), [1, 2, 4, 8, 11, 13], [3, 15, 16, 17, 20, 21, 22, 23, 24]],
                       'ɹ': [(7, 7), [1, 2, 4, 8, 14, 16], [3, 20, 21, 22, 23, 24]],
                       'ɻ': [(11, 7), [0, 1, 2, 4, 8, 14], [3, 20, 21, 22, 23, 24]],
                       'j': [(13, 7), [1, 2, 4, 8, 19, 20, 22, 24], [15, 16, 17]],
                       'l': [(7, 8), [0, 1, 2, 4, 8, 14, 15, 18], [3, 20, 21, 22, 23, 24]],
                       'ɭ': [(11, 8), [0, 1, 2, 4, 8, 14, 18], [3, 20, 21, 22, 23, 24]],
                       'ʎ': [(13, 8), [0, 1, 2, 4, 8, 14, 16, 18, 19, 20, 22], [3, 24]],
                       'ʟ': [(15, 8), [0, 1, 2, 4, 8, 19, 20], [15, 16, 17, 22, 23, 24]],
                       'i': [(23, 0), [25, 20, 22, 24], []],
                       'y': [(24, 0), [25, 20, 22, 24, 12], []],
                       'ɨ': [(27, 0), [25, 20, 24], []],
                       'ʉ': [(28, 0), [25, 20, 24, 12], []],
                       'ɯ': [(30, 0), [25, 20, 23, 24], []],
                       'u': [(31, 0), [25, 20, 23, 24, 12], []],
                       'ɪ': [(25, 1), [25, 20, 22], []],
                       'ʏ': [(26, 1), [25, 20, 22, 12], []],
                       'ʊ': [(29, 1), [25, 20, 23, 12], []],
                       'e': [(23, 2), [25, 22, 24], []],
                       'ø': [(24, 2), [25, 22, 24, 12], []],
                       'ɘ': [(27, 2), [25, 24], []],
                       'ɵ': [(28, 2), [25, 24, 12], []],
                       'ɤ': [(30, 2), [25, 23, 24], []],
                       'o': [(31, 2), [25, 23, 24, 12], []],
                       'ɛ': [(23, 4), [25, 22], []],
                       'œ': [(24, 4), [25, 22, 12], []],
                       'ə': [(27, 3), [25], []],
                       'ɞ': [(28, 4), [25, 12], []],
                       'ʌ': [(30, 4), [25, 23], []],
                       'ɔ': [(31, 4), [25, 23, 12], []],
                       'æ': [(23, 5), [25, 21, 22], [24]],
                       'a': [(23, 6), [25, 21], [24]],
                       'ɶ': [(24, 6), [25, 21, 22, 12], [24]],
                       'ɑ': [(30, 6), [25, 21, 23], [24]],
                       'ɒ': [(31, 6), [25, 21, 23, 12], [24]],
                       'w': [(23, 8), [1, 2, 4, 8, 11, 12, 19, 20, 23, 24], [3, 15, 16, 17]],
                       'ʍ': [(24, 8), [2, 3, 9, 11, 12, 19, 20, 23, 24], [15, 16, 17]],
                       'ɥ': [(25, 8), [1, 2, 4, 8, 11, 12, 19, 20, 22, 24], [3, 15, 16, 17]],
                       'ɕ': [(26, 8), [0, 2, 3, 14, 15, 16, 17, 19, 20, 22], [24]],
                       'ʑ': [(27, 8), [0, 2, 3, 8, 14, 15, 16, 17, 19, 20, 22], [24]],
                       't͡ɕ': [(28, 8), [0, 3, 14, 15, 16, 17, 19, 20, 22], [24]],
                       'd͡ʑ': [(29, 8), [0, 3, 8, 14, 15, 16, 17, 19, 20, 22], [24]]}

        self.classes = ['consonantal', 'sonorant', 'continuant', 'delayed release', 'approximant', 'tap', 'trill',
                        'nasal', 'voice', 'spread glottis', 'constricted glottis', 'labial', 'round', 'labiodental',
                        'coronal', 'anterior', 'distributed', 'strident', 'lateral', 'dorsal', 'high', 'low', 'front',
                        'back', 'tense', 'syllabic']

        self.class_descriptions = {'consonantal': 'radical constriction in the vocal tract | +: liquids, nasals, '
                                               'fricatives, affricates, stops | -: vowels, glides',
                                   'sonorant': 'spontaneous voicing is possible | +: vowels, glides, liquids, nasals | '
                                               '-: fricatives, affricates, stops (obstruents)',
                                   'continuant': 'airflow out of the mouth is continuous | +: vowels, glides, liquids,'
                                                 'fricatives | -: nasals, affricates, stops',
                                   'delayed release': 'release produces frication (obstruents only) | +: fricatives, '
                                                      'affricates, | -: stops',
                                   'approximant': 'frictionless escape of air out of the mouth | +: vowels, glides, '
                                                  'liquids | -: nasals, fricatives, affricats, stops',
                                   'tap': 'tapping of articulator | +: taps | -: all other consonants',
                                   'trill': 'trilling of articiulator | +: trills | -: all other consonants',
                                   'nasal': 'airflow out of the nasal cavity | +: nasals | -: other',
                                   'voice': 'vibration of the vocal cords | +: voiced sounds | -: voiceless sounds',
                                   'spread glottis': 'vocal folds held far apart | +:  aspirated consonants, breathy '
                                                     'vowels, glottal fricatives | -: all other sounds',
                                   'constricted glottis': 'narrow or closed glottis | +: ejectives, glottal stop, '
                                                          'creaky voice, preglottalized sounds | -: all other sounds',
                                   'labial': 'articulated with lips | +: bilabials, labiodentals | -: all other '
                                             'consonants',
                                   'round': 'articulated with lips rounded | +: rounded labials | -: all other '
                                            'consonants (except secondary rounding)',
                                   'labiodental': 'articulated with lower lip on upper teeth | +: labiodentals | -: all '
                                                  'other consonants',
                                   'coronal': 'articulated with the tongue blade or tip | +: dentals, alveolars, '
                                              'palato-alveolars, retroflexes, palatals | -: all other consonants',
                                   'anterior': 'articulated at alveolar ridge or forward (coronals only) | +: dentals, '
                                               'alveolars | -: palato-alveolars, retroflexes, palatals',
                                   'distributed': 'articulated with tongue blade (coronals only) | +: dentals, '
                                                  'palato-alveolars, palatals | -: alveolars, retroflexes',
                                   'strident': 'air channeled through tongue at teeth (coronals only) | +: '
                                               'alveolar/palato-alveolar/alveolopalatal fricatives and affricates | -: '
                                               'all other coronals (non-sibilants)',
                                   'lateral': 'air passes around the sides of the tongue | +: laterals | -: '
                                              'all other consonants',
                                   'dorsal': 'articulated with the tongue body | +: velars, uvulars, pharyngeals | '
                                             '-: all other consonants',
                                   'high': 'tongue above neutral position | +: high vowels | -: low and mid vowels',
                                   'low': 'tongue below neutral position | +: low vowels | -: high and mid vowels',
                                   'front': 'tongue fronted | +: front vowels | -: back and central vowels',
                                   'back': 'tongue retracted | +: back vowels | -: front and central vowels',
                                   'tense': 'longer duration, higher height (mid and high vowels only) | +: tense '
                                            'vowels | -: lax vowels',
                                   'syllabic': 'can be the peak/nucleus of a syllable | +: vowels | -: consonants'}

        self.screen = screen  # create the window
        self.screen.wm_title("Feature Classes")

        self.buttons = []
        self.frames = []

        self.selected_phones = []

        self.selected_features = []

        self.ipa_chart = tk.Frame(self.screen, padx=20, pady=20)  # create the frame for the IPA
        self.ipa_chart.pack()
        self.ipa_chart.columnconfigure(22, minsize=30)

        self.feature_chart = tk.Frame(self.screen, padx=20, pady=20)
        self.feature_chart.pack()

        self.entry = tk.Frame(self.screen)
        self.entry.pack(fill=X)

        self.phone_entry = tk.Frame(self.entry)  # create the frame for the phones
        self.phone_entry.pack(side=LEFT, expand=True)
        self.button_frame = tk.Frame(self.entry)  # create the frame for the clear button
        self.button_frame.pack(side=LEFT, expand=True)
        self.feature_entry = tk.Frame(self.entry)  # create the frame for the features
        self.feature_entry.pack(side=RIGHT, expand=True)

        self.out_frame = tk.Frame(self.screen)  # create the frame for the output data
        self.out_frame.pack()

        for i in range(len(self.phones)):
            button_text = self.ordered_phones[i]

            frame = tk.Frame(self.ipa_chart, width=30, height=30, borderwidth=1, relief=RIDGE)
            frame.propagate(False)
            frame.grid(row=self.phones[button_text][0][1], column=self.phones[button_text][0][0], sticky="nsew")

            button = tk.Button(frame, text=button_text, borderwidth=0, bg="#77DD77", activebackground="#575A61",
                               activeforeground="#D0DB97", command=partial(self.add_phone, button_text),
                               font=('Doulos SIL', 14))
            button.pack(expand=True, fill=BOTH)

            self.frames.append(frame)
            self.buttons.append(button)

        for feature in self.classes:
            frame = tk.Frame(self.feature_chart, relief=RIDGE, borderwidth=1)
            frame.pack(expand=True, fill=BOTH, side=LEFT)
            button = tk.Button(frame, text=feature, borderwidth=0, bg="#77DD77", activebackground="#575A61",
                               activeforeground="#D0DB97", command=partial(self.add_feature, feature))
            button.pack(expand=True, fill=BOTH, side=LEFT)

        self.phone_text = tk.Label(self.phone_entry)
        self.phone_text.config(text="Selected Phones: \n")
        self.phone_text.pack(side=LEFT)

        """
        self.phone_frame = tk.Frame(self.button_frame, relief=RIDGE, borderwidth=1)
        self.phone_frame.pack(side=LEFT)
        self.phone_button = tk.Button(self.phone_frame, text="Calculate features", borderwidth=0, bg="#77DD77",
                                      activebackground="#575A61", activeforeground="#D0DB97",
                                      command=self.display_phone)
        self.phone_button.pack()
        """

        self.clear_frame = tk.Frame(self.button_frame, relief=RIDGE, borderwidth=1)
        self.clear_frame.pack(side=LEFT)
        self.clear_button = tk.Button(self.clear_frame, text="Clear", borderwidth=0, bg="#77DD77",
                                      activebackground="#575A61",
                                      activeforeground="#D0DB97", command=self.clear)
        self.clear_button.pack(expand=True, fill=Y, side=LEFT)

        """
        self.feature_frame = tk.Frame(self.button_frame, relief=RIDGE, borderwidth=1)
        self.feature_frame.pack(side=LEFT)
        self.feature_button = tk.Button(self.feature_frame, text="Calculate phones", borderwidth=0, bg="#77DD77",
                                        activebackground="#575A61", activeforeground="#D0DB97",
                                        command=self.display_feature)
        self.feature_button.pack()
        """

        self.feature_text = tk.Label(self.feature_entry)
        self.feature_text.config(text="Selected Features: \n")
        self.feature_text.pack(side=LEFT)

        self.output_text = tk.Label(self.out_frame)
        self.output_text.config(font=('Doulos SIL', 12), justify=LEFT)
        self.output_text.pack()

    # Finds sounds containing the features
    def find_sounds(self, features):
        output = []

        if len(features) == 0:
            return []

        for feature in features:
            if feature not in self.classes:
                raise Exception("Feature {} does not exist".format(feature))

        for phone in self.ordered_phones:
            if all(self.classes.index(feature) in self.phones[phone][1] for feature in features):
                output.append(phone)

        output.sort(key=lambda x: self.ordered_phones.index(x))
        return output

    # Find the zeros for the sound
    def find_zeros(self, sounds):
        if len(sounds) == 0:
            return []

        output = self.phones[sounds[0]][2]

        for sound in sounds[1:]:
            output = [s for s in output if s in self.phones[sound][2]]

        return output

    # Finds the features common in the sounds
    def find_feature(self, sounds):
        if len(sounds) == 0:
            return []

        output = self.phones[sounds[0]][1]

        for sound in sounds[1:]:
            output = [s for s in output if s in self.phones[sound][1]]

        return output

    def add_phone(self, phone):
        if phone not in self.selected_phones:
            self.selected_phones.append(phone)
        self.phone_text.config(text="Selected Phones: \n{}".format(" ".join(self.selected_phones)))
        self.display_phone()

    def add_feature(self, feature):
        if feature not in self.selected_features:
            self.selected_features.append(feature)
        self.feature_text.config(text="Selected Features: \n{}".format(", ".join(self.selected_features)))
        self.display_feature()

    def clear(self):
        self.selected_phones = []
        self.selected_features = []
        self.phone_text.config(text="Selected Phones: \n{}".format(" ".join(self.selected_phones)))
        self.feature_text.config(text="Selected Features: \n{}".format(", ".join(self.selected_features)))
        self.output_text.config(text="")

    def display_phone(self):
        output_nums = self.find_feature(self.selected_phones)
        output = [self.classes[i] for i in output_nums]
        zeros = self.find_zeros(self.selected_phones)
        zeros = [self.classes[i] for i in zeros]
        if len(output) == 0 and len(zeros) == 0:
            output_text = "no similar features"
        elif len(output) > 0 and len(zeros) > 0:
            output_text = "[+{}, 0{}]".format(", +".join(output), ", 0".join(zeros))
        elif len(zeros) == 0:
            output_text = "[+{}]".format(", +".join(output))
        else:
            output_text = "[0{}]".format(", 0".join(zeros))

        output_text += "\n"

        if len(self.selected_phones) > 1:
            for phone in self.selected_phones:
                append = [feature for feature in self.find_feature([phone]) if feature not in output_nums]
                append = [self.classes[i] for i in append]
                if len(append) > 0:
                    output_text += phone
                    output_text += ": "
                    output_text += "+{}".format(" +".join(append))
                    output_text += "\n"

        self.output_text.config(text=output_text)

    def display_feature(self):
        output = self.find_sounds(self.selected_features)
        if len(output) == 0:
            output_text = "no phones \n"
        else:
            output_text = "/{}/".format("/ /".join(output))
            output_text += "\n"

        for feature in self.selected_features:
            output_text += feature + ": "
            output_text += self.class_descriptions[feature]
            output_text += "\n"

        self.output_text.config(text=output_text)


root = Tk()
my_main = Main(root)
root.mainloop()
