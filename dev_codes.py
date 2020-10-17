import recipe_manager as rm
import asset_manager as am

'''
####################################################
#####WARNING DONT RUN BOTH  THE MODULES AT ONCE#####
#COMMENT THE OTHER MODULES WHICH YOU ARENT CHECKING#
####################################################

###############################################
# dev code to iterate through all recipes
# to check if any recipe fails to parse
x = rm.recipe_loader()
print(len(x))
i = 0

for iterator in x:
    try:
        y = rm.unique_items_required(iterator)
        # print(i)
        i += 1
    except:
        print("failed", iterator)
###############################################

###############################################
# dev code to iterate through all recipes
# to check if any recipe fails to parse
x = rm.r_name()
print(len(x))

i = 0

for iterator in x:
    try:
        s = rm.slot_item(iterator)
        # print(i)
        i += 1
    except:
        print("failed slot", iterator)
###############################################
'''
###############################################
# Dev code to log all recipes which failed to load due to meta data
# and logs the data in log.txt
x = rm.r_name()
print(len(x))
f = open("failed_log.txt", "w")

for iterator in x:
    try:
        grid = rm.slot_item(iterator)
        img_name_list = am.img_data_helper(grid)
        img_data_list = am.img_byte_data_converter(img_name_list)

    except:

        f.write(iterator)
        f.write("\n")

f.close()
###############################################
