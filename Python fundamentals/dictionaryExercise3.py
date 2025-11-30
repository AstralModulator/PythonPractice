inventory = {
    "weapons": {
        "melee": {
            "sword": {"damage": 50, "weight": 6},
            "dagger": {"damage": 25, "weight": 2}
        },
        "ranged": {
            "bow": {"damage": 35, "weight": 4},
            "crossbow": {"damage": 45, "weight": 7}
        }
    },

    "potions": {
        "healing": {"small": 3, "medium": 1},
        "mana": {"small": 5, "large": 2}
    }
}

print(inventory["weapons"]["ranged"]["crossbow"]["damage"])
inventory["weapons"]["melee"].update({"axe":{"damage": 60, "weight": 9}})
inventory["potions"]["healing"].update({"small": 5})
inventory["weapons"]["ranged"].pop("bow")

for key, values in inventory["weapons"]["melee"].items():
    print(f"{key} ->", end = " ")
    for key1,value in values.items():
        print(f"{key1}: {value}", end = ", ")
    print()

state = "Exists" if "large" in inventory["potions"]["mana"].keys() else "Not found"
print(state)

heaviest_category = ""
heaviest = ""
heaviest_weight = 0
for category,weapons in inventory["weapons"].items():
    for name,value in weapons.items():
        if  value["weight"] > heaviest_weight:
            heaviest_weight = value["weight"]
            heaviest = name
            heaviest_category = category

print(heaviest_category)
print(heaviest)
print(f"Heaviest weapon: {heaviest} -> {inventory["weapons"][heaviest_category][heaviest]}")

heaviest_weapon = max((weapon for cats in inventory["weapons"].values() for weapon in cats.values()), key = lambda w:w["weight"])
