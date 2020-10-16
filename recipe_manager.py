import json
import constants
import os

'''
    Method to Eliminate a list within a list of dictionaries in case of recipes involving items which can be intercahnged
    parameter list 
    returns a cleaned list containing only dictionaries
'''


def cleaning_list(unclean_list):

    clean_list = list()
    for iterator in unclean_list:
        if type(iterator) is dict:
            clean_list.append(iterator)

        else:
            clean_list.append(iterator[0])

    return clean_list


'''
    Method to identify unique ingredients required in an item
    Method's parameter is a string
    Returns a list of dictionary
'''


def unique_items_required(item_name):

    # Determining file path and creating the json object
    abs_file_path = constants.abs_recipe_dir + item_name + ".json"
    fhandle = open(abs_file_path).read()
    json_obj = json.loads(fhandle)

    # Initialising Lists and counter
    unique_ingredients = []
    unique_ingredients_list = []

    # Code Logic for shaped and shapeless which Generates the unique item list
    if json_obj["type"] == "crafting_shaped":
        for item in json_obj["key"]:
            unique_ingredients_list.append(json_obj["key"][item])

    else:
        for item in json_obj["ingredients"]:
            if item not in unique_ingredients_list:
                unique_ingredients_list.append(item)

    # Logic to eliminate multiple items possibilties and convert non-dictionary entries into dictionary
    unique_ingredients = cleaning_list(unique_ingredients_list)

    return unique_ingredients


# x = unique_items_required("beacon")
# unique_items_required("fire_charge")
# print(x)

'''
    Loads all the recipe's file names
    No parameter
    returns list of filenames
'''


def recipe_loader():

    # "w" creates new file in write mode overwrites if already exist
    shapeless = list()
    shaped = list()
    f_recipe = list()
    file_names = list()

    # reads the files in the folder
    for filename in os.listdir(constants.abs_recipe_dir):

        abs_file_path = constants.abs_recipe_dir + filename
        read_data = open(abs_file_path).read()  # File Handle
        data = json.loads(read_data)  # Json object

        # Categorising into shaped and shapeless recipes
        if data["type"] == "crafting_shapeless":
            shapeless.append(filename)

        else:
            shaped.append(filename)

        # Listing all the recipes Available
        if data["result"]:
            fname = data["result"]["item"]
            fname = fname.replace("minecraft:", "")
            f_recipe.append(fname)
        tmp_file_name = filename.replace(".json", "")
        file_names.append(tmp_file_name)

    return file_names


'''
    Method to determine if the item is shaped or shapeless
    parameter  Item_name
    returns string (Shape/shapeless)
'''


def recipe_shape_helper(item_name):

    item_path = constants.abs_recipe_dir + item_name + ".json"
    fhandle = open(item_path).read()
    json_obj = json.loads(fhandle)

    if json_obj["type"] == "crafting_shaped":
        return "shaped"
    else:
        return "shapeless"


'''
    method to convert the unique item dictionary into a list
    parameter unique_item_dictionary
    returns unique_item_list
'''


def unique_item_list_converter(u_dict):

    u_items = list()
    unique_item_list = list()
    for items in u_dict:
        u_items.append(items['item'])
    for x in u_items:
        y = x.replace("minecraft:", "")
        unique_item_list.append(y)
    return unique_item_list
