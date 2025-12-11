class Animal:
    def sleep(self):
        return "is Sleeping"

class Prey(Animal):
    name = "Prey"
    def sleep(self):
        print(f"{Prey.name} {super().sleep()}")
    def flee(self):
        print("Prey is fleing")
class Predator(Animal):
    name = "Predator"
    def sleep(self):
        print(f"{Predator.name} {super().sleep()}")
    def hunt(self):
        print("Predator is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
rabbit.flee()
rabbit.sleep()