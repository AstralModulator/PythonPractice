students = {
    "Luna": {"math": 92, "science": 88},
    "Rai": {"math": 76, "science": 81},
    "Astra": {"math": 85, "science": 90}
}

english = 90
for value in students.values():
    value.update({"english":english})
    english += 1

students.update({"Nova":{"math": 90, "science": 87, "english": 95}})
students["Rai"].update({"science":students["Rai"]["science"]+5})

for key,values in students.items():
    print(f"{key}: ")
    for key1,value in values.items():
        print(f"      {key1}: {value}")

inventory = {
    "weapons": {
        "swords": ["Katana", "Longsword"],
        "bows": ["Shortbow"]
    },
    "potions": {
        "health": 5,
        "mana": 2
    },
    "gold": 320
}

inventory["weapons"]["bows"].append("Greatbow")
inventory["weapons"]["swords"].remove("Longsword")
inventory.update({"materials":["Iron","Silver"]})

total_items = len(inventory["weapons"]["swords"]) + len(inventory["weapons"]["bows"]) + len(list(inventory["potions"].keys())) + len(inventory["materials"])

print(f"Total items: {total_items}")

for key,value in inventory.items():
    print(f"{key}: {value}")


users = {
    "001": {"name": "Astra", "roles": ["admin", "editor"]},
    "002": {"name": "Dip", "roles": ["player"]},
    "003": {"name": "Loki", "roles": ["banned", "player"]},
    "004": {"name": "Nova", "roles": ["moderator"]}
}

state = "User found" if any(v["name"] == "Astra" for v in users.values()) else "User not found"
print(state)

players = [v["name"] for v in users.values() if "player" in v["roles"]]
print(*players, sep = "\n")

users = {
    "001": {"name": "Astra", "roles": ["admin", "editor"]},
    "002": {"name": "Dip", "roles": ["player"]},
    "003": {"name": "Loki", "roles": ["banned", "player"]},
    "004": {"name": "Nova", "roles": ["moderator"]}
}

state = "There is at least one banned user" if any("banned" in v["roles"] for v in users.values()) else "No banned users"
print(state)
admins = [v["name"] for v in users.values() if "admin" in v["roles"]]
print(*admins, sep = "\n")