thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(thisdict["brand"]) # Ford
# print(thisdict.get('brand')) # Ford
# print(thisdict.keys()) # it's helps to print keys -> dict_keys(['brand', 'model', 'year'])

# print(thisdict["brand2"]) # this show typeerror
# print(thisdict.get('brand2')) # None

# ----------------------------------------------------------------------------------
dic = {
    344: "Harry",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}

# print(dic[567]) # Neha
# print(dic.keys()) # dict_keys([344, 56, 678, 567])
# print(dic.values()) # it's helps to print values -> dict_values(['Harry', 'Shubham', 'Zakir', 'Neha'])

# for key in dic.keys():
#     print(dic[key]) # it helps to print keys value -> Harry, Shubham, Zakir, Neha


# for key in dic.keys():
#     print(f"The value corresponding to the key {key} is {dic[key]}") # it helps to print keys and values ->The value corresponding to the key 344 is Harry
                                                                                                          # The value corresponding to the key 56 is Shubham
                                                                                                          # The value corresponding to the key 678 is Zakir
                                                                                                          # The value corresponding to the key 567 is Neha


print(dic.items()) # dict_items([(344, 'Harry'), (56, 'Shubham'), (678, 'Zakir'), (567, 'Neha')])

for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
