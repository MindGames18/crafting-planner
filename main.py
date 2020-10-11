# immu
import extracting_assets as ea
import PySimpleGUI as sg
import deleting_assets

layout = [[sg.Text('Version Selector.')],
          [sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values[0]

try:
    ea.extracting_assets(text_input)
    sg.popup('Assets Extracted', text_input)

except:
    sg.popup('File doesnt exist, Assets could not be extracted', text_input)
    exit()
deleting_assets.delete_assets()
