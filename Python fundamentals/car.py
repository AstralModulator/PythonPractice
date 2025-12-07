class Car:
    def __init__(self,model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed
    def start_engine(self):
        print(f"You started your {self.model}'s engine.")
    def stop_engine(self):
        print(f"You stopped the engine.")
