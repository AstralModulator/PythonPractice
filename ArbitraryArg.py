# Arbitrary Arguments

def add_num(*args):
    sum = 0
    for arg in args:
        sum += arg
    return f"The sum of your given numbers is: {sum}"

print(add_num(1,2,3,4,5,6))


# def disp_name(**kwargs):
#     return f"Your name is: {kwargs.get("first")} {"" if kwargs.get("middle") == None else kwargs.get("middle")} {kwargs.get("last")}"
#
# print(disp_name(first = "Dip", last = "Limbu"))

# def disp_name(*args):
#     for arg in args:
#         print(arg.capitalize(),end =" ")
#
# disp_name("dip","kiran","limbu")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street = "123 Fake St.", city = "Detroit", state = "MI", zip = "54321")