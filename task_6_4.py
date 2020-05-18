class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f"{self.color} {self.name} started"

    def stop(self):
        return f"{self.color} {self.name} stopped"

    def turn_left(self):
        return f"{self.color} {self.name} turned left."

    def turn_right(self):
        return f"{self.color} {self.name} turned right."

    def turn_back(self):
        return f"{self.color} {self.name} turned back. The driver might forget something at home."

    def show_speed(self): #Текущая скорость
        return f"{self.color} {self.name} is driving {self.speed} km per hour."

class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"You're over-speeding!!! Slow down by {self.speed - 60} km/h."
        else:
            return f"Speed of {self.speed} is ok. Keep going!"

class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def sport(self):
        return f"{self.color} {self.name} is engaged sport mode. The speed is increased by 20% from {self.speed} up to {self.speed*1.2} km/h."

class WorkCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"You're over-speeding!!! Slow down by {self.speed - 40} km/h."
        else:
            return f"Speed of {self.speed} is ok. Keep working!"

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def police_car(self):
        if self.is_police:
            return f"{self.color} {self.name} is a police car"
        else:
            return f"{self.color} {self.name} is NOT a police car."

car_1 = TownCar("BMW", "Red", 63, False)
car_2 = SportCar("Lamborghini Huracan", "Yellow", 300, False)
car_3 = WorkCar("Ford Focus", "Silver", 78, False)
car_4 = PoliceCar("UAZ Hunter", "White", 40, True)

print(f"{car_1.go()} with the speed of {car_1.speed}. {car_1.show_speed()}")
print(f"{car_4.police_car()}. {car_4.stop()} just round the corner.")
print(f"{car_2.go()}. {car_2.show_speed()}")
print(f"{car_2.sport()}")
print(f"Police car - {car_4.color} {car_4.name} is now in pursuit of {car_2.color} {car_2.name}")
print(f"Suddenly {car_1.turn_back()}")
print(f"{car_3.go()}, then {car_3.turn_right()} {car_3.show_speed()}")

