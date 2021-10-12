import numpy as np
import string

text = np.array(['Th   Is', '{Is', 'Al+mOst', 'A}', 'nOr m   Al!!!', 'sEnt578EncE', '-nOw'])  # Do not change this.


def remove_extra_stuff(txt):
    return np.char.translate(txt, str.maketrans('AEIOUY', 'aeiouy', string.punctuation + string.digits + string.whitespace))


if __name__ == '__main__':
    for word in remove_extra_stuff(text):
        print(word, end=" ")
