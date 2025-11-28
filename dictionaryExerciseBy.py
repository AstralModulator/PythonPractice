person = {
    "name": "Astra",
    "age": 21,
    "city": "Kathmandu"
}
print(person.get("name"))
person.update({"hobby":"gaming"})
person.update({"age":20})
person.pop("city")
for key in person.keys():
    print(key)
for key,value in person.items():
    print(f"{key}: {value}")

students = {
    "001": {
        "name": "Luna",
        "marks": {"math": 92, "science": 88}
    },
    "002": {
        "name": "Rai",
        "marks": {"math": 76, "science": 81}
    }
}

print(students["001"]["marks"]["math"])
students.get("001").get("marks").update({"english":90})
students["002"].update({"name":"Rai Bishal"})
students.update({"003":{
    "name" : "Dip Kiran",
    "marks" : {"DBMS": 80, "ITA":78}
}})
for key,values in students.items():
    print(f"{key}:")
    for value in values:
        print(f"{value}: {values[value]}")


data = {
    "users": {
        "active": {
            "count": 3,
            "list": ["Dip", "Astra", "Nova"]
        },
        "banned": {
            "count": 1,
            "list": ["Loki"]
        }
    }
}
data["users"]["active"]["list"].append("Ghost")
data["users"]["active"]["list"].remove("Astra")
data["users"]["active"].update({"count":len(data["users"]["active"]["list"])})

print("Active Users: ")
for user in data["users"]["active"]["list"]:
    print(user)

status = "User not found"
for value in data["users"].values():
    if "Zen" in value['list']:
        status = "User found"
        break

print(status)