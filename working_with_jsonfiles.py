#!/usr/bin/env python3.7

import json

## Read JSON file

json_file="example.json"

fo=open(json_file,'r')
print(json.load(fo))   ## Provides dictionary data form 
fo.close()


## Write to JSON file

my_info={'Name': 'Mohan','Skills': ['Linux', 'Shell', 'Devops', 'Python']}

fo=open("myinfo.json",'w')
json.dump(my_info,fo,indent=4)
fo.close()

