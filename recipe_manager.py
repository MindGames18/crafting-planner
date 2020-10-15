import json
import constants
import json_read

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
    for iterator in unique_ingredients_list:
        if type(iterator) is dict:
            unique_ingredients.append(iterator)

        else:
            unique_ingredients.append(iterator[0])

    return unique_ingredients


# unique_items_required("beacon")
# unique_items_required("fire_charge")
# print(type(x))
