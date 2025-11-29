# Keyword arguments

# def greet_user(greetings, title, first, last):
#     return f"{greetings} {title} {first} {last}"
#
# print(greet_user("Hello!",title = "Mrs.", last = "Limbu", first = "Dip Kiran"))
#
#
# for x in range(1,11):
#     print(x,end = " ")
#
# print()
# print("1","2","3",sep = "-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

print(get_phone(country = "+1", area = 123, first = 980, last = 2841))