num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def add_num(num1,num2):
    return num1+num2
print(f"Adding the two numbers: {add_num(num1,num2)}")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

def construct_name(first_name,last_name):
    return f"Your constructed name is {first_name.capitalize()} {last_name.capitalize()}"

print(construct_name(first_name,last_name))