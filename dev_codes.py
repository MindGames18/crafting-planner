import recipe_manager as rm
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