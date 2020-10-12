import os
import json 

script_dir = os.path.dirname(__file__)
sub_dir = '\\jar\\assets\\minecraft\\recipes\\'
filename = 'sugar.json'

abs_file_path = script_dir + sub_dir + filename

read_data = open(abs_file_path).read()                        #reads the file
data = json.loads(read_data)                                  #loads everything in the file
print(data["key"])

y=list()
for x in data["key"]:
    y.append(x)

for z in y:
    print(type(data["key"][z]))
exit()
print(data["key"][z]["item"])    
exit()
for i in data:
    if i == "key":
        print(data["key"])
        for j in key:
            print(data["key"][j])