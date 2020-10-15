import asset_manager as am
import PySimpleGUI as sg
import recipe_manager as rm

'''
    The asset loader UI
'''


def loader_gui():
    sg.theme('BluePurple')

    version_list = ['1.12.2', 'WIP - NO USES']

    # The GUI Layout
    layout = [[sg.Text('Choose Your Minecraft Version'), sg.Text(size=(10, 1), key='-OUTPUT-')],
              [sg.Image(filename=None)],
              [sg.OptionMenu((version_list),
                             key='selected_version', tooltip='Version')],
              [sg.Button('Load'), sg.Button('Exit'), sg.Button('Delete Local Cache')]]

    # Window Creation
    window = sg.Window('Minecraft Loader', layout, size=(250, 100))

    #---------- The Beginnning of Event Loop ----------#
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
        #---------- The End of Event Loop ----------#


'''
    The Main UI method
    No parametres
    No returns
'''


def main_ui():
    sg.theme('BluePurple')

    # Checking if Assets have been loaded already
    try:
        available_recipes = rm.recipe_loader()
        available_recipes.sort()
    except:
        loader_gui()
        available_recipes = rm.recipe_loader()
        available_recipes.sort()

    # Coloumn Element
    col = [
        [sg.Button(button_text='', size=(15, 6), border_width=5,
                   image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='AA'), sg.Button(button_text='', size=(15, 6), border_width=5, image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='BB'), sg.Button(button_text='', size=(15, 6), border_width=5, image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='CC')],
        [sg.Button(button_text='', size=(15, 6), border_width=5,
                   image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='DD'), sg.Button(button_text='', size=(15, 6), border_width=5, image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='EE'), sg.Button(button_text='', size=(15, 6), border_width=5, image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='FF')],
        [sg.Button(button_text='', size=(15, 6), border_width=5,
                   image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='GG'), sg.Button(button_text='', size=(15, 6), border_width=5, image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='HH'), sg.Button(button_text='', size=(15, 6), border_width=5, image_filename='apple_template.png', image_data=None, disabled=False, tooltip=None, pad=(15, 15), button_color=('white', 'white'), key='II')]
    ]
    # The layout of the UI
    layout = [
        [sg.Text('Minecraft Recipe Viewer', size=(
            42, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Combo(available_recipes, font=('Helvetica', 11), readonly=True,
                  key='recipe_item', size=(30, 1), enable_events=True)],
        [sg.Frame('Output', [[sg.Text("Sample Output area", size=(30, 30))]]),
         sg.Column(col, background_color='black')],

        [sg.Button(button_text="Reset", key="empty_grid"), sg.Button(
            button_text='Asset Loader'), sg.Button('Exit')]
    ]

    # Window Creation
    window = sg.Window('Minecraft Recipe Viewer', layout, size=(800, 650))

    #---------- The Beginnning of Event Loop ----------#
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break

        if event == 'Asset Loader':
            loader_gui()

        # User Generated event when they select an item from the list
        if event == 'recipe_item':

            recipe_item = values['recipe_item']
            unique_item_dictionary = rm.unique_items_required(recipe_item)
            unique_item_list = rm.unique_item_list_converter(unique_item_dictionary)

            for item in unique_item_list :
                
            # Helper to determine shaped/shapeless
            recipe_type = rm.recipe_shape_helper(recipe_item)

            if recipe_type == "shapeless":
                print('sha')

        if event == 'empty_grid':
            grid_elements = ['AA', 'BB', 'CC',
                             'DD', 'EE', 'FF', 'GG', 'HH', 'II']
            for items in grid_elements:
                window[items].update(image_filename='empty_template.png')

    #---------- The End of Event Loop ------------------#


main_ui()
