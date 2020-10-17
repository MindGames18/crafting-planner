import os

'''
    All Recurring Constants go in this file. Do not Forget to invoke "import constants" in any python file you need this

'''

# Directory Related constants
script_dir = os.path.dirname(__file__)
jar_dir = "\\jar"
recipe_dir = "\\assets\\minecraft\\recipes\\"

abs_recipe_dir = script_dir + jar_dir + recipe_dir
texture_dir = "\\assets\\minecraft\\textures\\items\\"
abs_texture_dir = script_dir + jar_dir + texture_dir

texture_block_dir = "\\assets\\minecraft\\textures\\blocks\\"
abs_texture_block_dir = script_dir + jar_dir + texture_block_dir
