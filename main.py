# 1
class Transport:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def move(self):
        print(f"Transport {self.speed} tezlikda {self.fuel} yoqilgi bilan harakat")



class Car(Transport):
    def __init__(self, brand, speed, fuel, color):
        super().__init__(speed, fuel)
        self.brand = brand
        self.color = color


    def move(self):
        super().move()
        print(f"Car {self.brand}, rang: {self.color}")



m1 = Car(brand="BMW", speed=150, fuel=30, color="Qora")
m1 = move()
