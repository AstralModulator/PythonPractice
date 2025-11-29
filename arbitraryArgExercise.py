def shipping_labels(*args, **kwargs):
    for arg in args:
        print(arg.capitalize(),end = " ")
    print()
    if not "pobox" in kwargs:
        print(f"{kwargs['street']} {'' if kwargs.get('apt') == None else kwargs['apt']}")
    else:
        print(kwargs.get("street"))
        print(kwargs['pobox'])
    print(f"{kwargs['city']} {kwargs['state']} {kwargs['zipcode']}")



shipping_labels("Dr.", "SpongeBob", "Squarpants",
                    street = "Herald St.",
                    city = "San Diego",
                    state = "CA",
                    zipcode = "9410"
                )