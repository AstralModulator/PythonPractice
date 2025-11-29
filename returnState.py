num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def add_numbers(num1,num2):
    return num1 + num2
print(f"Addition: {add_numbers(num1,num2)}")

#Create a Name

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

def construct_name(first_name,last_name):
    return first_name.capitalize() + " " + last_name.capitalize()

print(f"Your constructed name comes out to be:{construct_name(first_name,last_name)} ")