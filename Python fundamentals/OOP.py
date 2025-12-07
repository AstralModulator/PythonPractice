#class and objects
class Car:
    def __init__(self,model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed
    def start_engine(self):
        print(f"You started your {self.model}'s engine.")
    def stop_engine(self):
        print(f"You stopped the engine.")

car1 = Car("Mercede", "red", 5)
print(car1.speed)
car1.start_engine()
