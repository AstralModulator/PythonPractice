my_dict = {"USA":"Washington","UK":"London","Nepal":"Kathmandu","India":"New Delhi"}

print(my_dict)
print(my_dict.get("USA"))
my_dict.update({"China":"Beijing"})
print(my_dict)
my_dict.pop("USA")
my_dict.popitem()
print(my_dict)
keys = my_dict.keys()

for key in my_dict.keys():
    print(my_dict.get(key))

for key,value in my_dict.items():
    print(f"{key}: {value}")

