# Fill in this file with the code from parsing JSON exercise
import json
import yaml
with open('onder.json','r') as json_file:
 ourjson = json.load(json_file)
print("Adı: {}".format(ourjson['kimlik']['ad']))
print("SoyAdı: {}".format(ourjson['kimlik']['soyad']))
