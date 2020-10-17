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

    grid_elements = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II']

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

            # Generating the Unique item dictionary
            unique_item_dictionary = rm.unique_items_required(recipe_item)

            # Converting the Dictinary to list
            unique_item_list = rm.unique_item_list_converter(
                unique_item_dictionary)

            # Loading and generating a list of  dictionary of {unique_item : byte_data_of_the_texture}

            grid = rm.slot_item(recipe_item)

            # Updating ToolTip
            for x in range(len(grid_elements)):
                window[grid_elements[x]].SetTooltip(grid[x])

            # Loading Textures into a similar list
            img_name_list = am.img_data_helper(grid)
            
            # Converting the Textures to Byte data and updating the window
            img_data_list = am.img_byte_data_converter(img_name_list)
            for x in range(len(grid_elements)):
                window[grid_elements[x]].update(image_data=img_data_list[x])

            # Helper to determine shaped/shapeless
            recipe_type = rm.recipe_shape_helper(recipe_item)

            if recipe_type == "shapeless":
                print('sha')

        if event == 'empty_grid':

            for items in grid_elements:
                window[items].update(image_filename='empty_template.png')
            #################### TEST PURPOSE CODE ONLY ####################
            # x =[0,0]
            # y=[0,0]
            # x[0] = "C:\\gitrepo\\crafting-planner\\jar\\assets\\minecraft\\textures\\items\\wheat.png"
            # x[1] = "C:\\gitrepo\\crafting-planner\\jar\\assets\\minecraft\\textures\\items\\carrot.png"
            # y[0] = am.convert_to_bytes(x[0])
            # y[1] = am.convert_to_bytes(x[1])
            # window['AA'].update(image_data = y[0])
            # window['BB'].update(image_data = y[1])
            #################### TEST PURPOSE CODE ONLY ####################
            #---------- The End of Event Loop ------------------#


main_ui()
