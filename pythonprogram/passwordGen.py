import random
import string
import PySimpleGUI as sg

upper=random.sample(string.ascii_uppercase,2)
lower= random.sample(string.ascii_lowercase,2)
digits= random.sample(string.digits,2)
Symbol=random.sample(string.punctuation,2)

total=upper+lower+digits+Symbol
total=random.sample(total,len(total))
total= ''.join(total)
print(total)


sg.theme('DarkBlue6')
sg.set_options(font='verdana 15')

layout=[
    [sg.Text('Uppercase:'),sg.Push(), sg.Input(size=15)],
    [sg.Text('Lowercase:'), sg.Push(),sg.Input(size=15)],
    [sg.Text('Digits:'), sg.Push(),sg.Input(size=15)],
    [sg.Text('Symbols:'), sg.Push(),sg.Input(size=15)],
    [sg.Button('Ok'),sg.Button('cancel')],
    [sg.Text('Password'),sg.Push(),sg.Multiline(size=15,no_scrollbar=True)]

]

window=sg.Window('Password Generator',layout)

window.read()

window.close()