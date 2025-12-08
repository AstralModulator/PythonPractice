#super function
class Vehicle:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self,model,brand,doors):
        super().__init__(model,brand)
        self.doors = doors
    def info(self):
        print(f"{super().info()} with {self.doors} doors")

def main():
    car1 = Car("Benz","Mercedes",4)
    car1.info()

if __name__ == '__main__':
    main()