#class varianbles
class Student:
    graduating_year = 2027
    student_num = 0
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Student.student_num += 1
    def introduce(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old.")

aviral = Student("Aviral", 21, "male")
print(aviral.name)
aviral.introduce()
print(Student.graduating_year)
print(Student.student_num)