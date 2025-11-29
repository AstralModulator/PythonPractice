my_dict = {"USA":"Washington","UK":"London","Nepal":"Kathmandu","India":"New Delhi"}

print(my_dict)
for key in my_dict.keys():
    print(f"{key}: {my_dict.get(key)}")
my_dict.update({"China":"Beijing"})
for key,value in my_dict.items():
    print(f"{key}: {value}")

