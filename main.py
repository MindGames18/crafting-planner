import extracting_assets as ea
import PySimpleGUI as sg
import deleting_assets

sg.theme('BluePurple')

version_list = ['1.12.2', 'WIP - NO USES']

# The GUI Layout
layout = [[sg.Text('Choose Your Minecraft Version'), sg.Text(size=(10, 1), key='-OUTPUT-')],
          [sg.OptionMenu((version_list), default_value=None,
                         key='selected_version',tooltip= 'Version')],
          [sg.Button('Load'), sg.Button('Exit'), sg.Button('Delete Local Cache')]]

window = sg.Window('Minecraft Loader', layout, size=(250, 100))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Event To load the Assets File into the cache
    if event == 'Load':
        version = values['selected_version']
        try:
            ea.extracting_assets(version)
            sg.popup('Assets Extracted')
        except:
            sg.popup("Assets Could Not be extracted")

    # Event To Delete the Cache files
    if event == "Delete Local Cache":
        try:
            deleting_assets.delete_assets()
            sg.popup("Local Cache Deleted")
        except:
            sg.popup("Could not delete local cache")

window.close()
