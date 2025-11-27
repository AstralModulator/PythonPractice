numpad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for collection in numpad:
    for num in collection:
        print(f"{num:<3}",end="")
    print()