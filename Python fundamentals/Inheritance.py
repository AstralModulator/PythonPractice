class Animal:
    def __init__(self,name, is_alive):
        self.name = name
        self.is_alive = is_alive
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def eats(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def speaks(self):
        print(f"{self.name} is barking.")


class Cat(Animal):
    def speaks(self):
        print(f"{self.name} is Meowing.")

dog = Dog("Scooby",True)
dog.sleep()
dog.eats()
dog.speaks()

cat = Cat("Bobby",True)
cat.speaks()