# import pandas as pd
# import os
# import json
# import jsbeautifier

# path = str(os.getcwdb())[2:-1]
# file = '/last/replace_sample.csv'
# # csvPath = path + file
# # file = pd.read_csv(csvPath)
# # for index, row in file.iterrows():
# #   print(row[1], row[2])

# beforePath = path + "/last/sample_in_160069.json"

# # contents = open(beforePath, "r").read() 
# # data = [json.loads(str(item)) for item in contents.strip().split('\n')]
# with open(beforePath,'r') as f:
#     s = f.read()
#     s = s.replace('\t','')
#     s = s.replace('\n','')
#     s = s.replace(',}','}')
#     s = s.replace(',]',']')
#     data = json.loads(s)
#     print(str(data))



import pandas as pd
import os
import json
import jsbeautifier
import simplejson

path = str(os.getcwdb())[2:-1]
file = '/last/replace_sample.xlsx'
# file = '/last/replace_sample.xlsx'
# csvPath = path + file
file = pd.read_excel(path + file)
# file = pd.read_csv(path + file)

# beforePath = path + "/last/sample_in_160069.json"
beforePath = path + "/last/sample_in_160069.json"

# opening json file
contents = open(beforePath, "r")
json_object = json.load(contents)
contents.close()
print(json_object["data"]["classes"])
    
print(json_object.keys())
print(json_object.values())

# # iterating csv file
# before = []
# after = []
# for index, row in file.iterrows():
#   before.append(row[1].split(":"))
#   after.append(row[2].split(":"))
#   # if thrid element is not none, add ******* tmrow

# for i in range(len(json_object["data"]["attributes"])):
#   print(json_object["data"]["attributes"][i])

# # writing json file
# with open('/home/moog/python/last/result.json', 'w') as outfile:
#   json.dump(json_object, outfile)

# import json

# f = open("/home/moog/python/last/sample_in_160069.json", "r")
# file = f.read()
# f.close()
# a = str('"result": ["kr"]')
# b = str('"result": ["en"]')
# print(a)
# print(b)
# file = file.replace(a, b)
# print(file)