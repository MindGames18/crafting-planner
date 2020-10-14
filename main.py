import asset_manager as am
import PySimpleGUI as sg
import json_read as jr

'''
    The asset loader UI
'''


def loader_gui():
    sg.theme('BluePurple')

    version_list = ['1.12.2', 'WIP - NO USES']

    # The GUI Layout
    layout = [[sg.Text('Choose Your Minecraft Version'), sg.Text(size=(10, 1), key='-OUTPUT-')],
              [sg.Image(filename=None)],
              [sg.OptionMenu((version_list), default_value=None,
                             key='selected_version', tooltip='Version')],
              [sg.Button('Load'), sg.Button('Exit'), sg.Button('Delete Local Cache')]]

    window = sg.Window('Minecraft Loader', layout, size=(250, 100))
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        # Event To load the Assets File into the cache
        if event == 'Load':
            version = values['selected_version']
            try:
                am.extracting_assets(version)
                sg.popup('Assets Extracted')
                break
            except:
                sg.popup("Assets Could Not be extracted")
            # Event To Delete the Cache files

        if event == "Delete Local Cache":
            try:
                am.delete_assets()
                sg.popup("Local Cache Deleted")
            except:
                sg.popup("Could not delete local cache")


'''
    The Main UI method 
'''


def main_ui():
    sg.theme('BluePurple')
    try:
        available_recipes = jr.recipe_loader()
        available_recipes.sort()
    except:
        loader_gui()
        available_recipes = jr.recipe_loader()
        available_recipes.sort()

    x = am.convert_to_bytes('apple.png')

    layout = [
        [sg.Text('Item Browser')],
        [sg.Combo(available_recipes, readonly=True,
                  key='recipe_item', size=(30, 1))],
        [sg.Button(button_text='Asset Loader'), sg.Button('Exit')],
        [sg.Button(button_text='1', size=(15, 6), border_width=5, image_filename='apple.png', image_data=None, key='a'), sg.Button(
            button_text='1', size=(15, 6), border_width=5), sg.Button(button_text='1', size=(15, 6), border_width=5)],
        [sg.Button(button_text='1', size=(15, 6), border_width=5), sg.Button(button_text='1', size=(
            15, 6), border_width=5), sg.Button(button_text='1', size=(15, 6), border_width=5)],
        [sg.Button(button_text='1', size=(15, 6), border_width=5), sg.Button(button_text='1', size=(
            15, 6), border_width=5), sg.Button(button_text='1', size=(15, 6), border_width=5)],
        [sg.Button(button_text="update")]
    ]
    window = sg.Window('Minecraft Recipe Viewer', layout, size=(800, 600))
    while True:  # Event Loop
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break

        if event == 'Asset Loader':
            loader_gui()

        if event == 'update':
            window['a'].update(image_data=x)


main_ui()
