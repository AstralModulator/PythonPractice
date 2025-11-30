#list comprehension

doubles = [number for number in range(1,21) if number%2==0]
print(*doubles,sep= " ")

triples = [number*3 for number in range(1,11)]
print(*triples,sep= " ")

fruits = ["apple","banana","orange","strawberry"]
Fruits = [fruit.capitalize() for fruit in fruits]
print(*Fruits,sep= " ")

grades = [80,90,20,30,40,50,12,14,17]
passed_students = [grade for grade in grades if grade>40]
print(*passed_students,sep= " ")