import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    new_car = Car(f"ABC-{i}", random.randint(150, 200))
    cars.append(new_car)

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        
        car.drive(1)
        
        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Reg Number':<12} | {'Max Speed':<10} | {'Final Speed':<12} | {'Distance':<10}")
print("-" * 55)

for car in cars:
    print(f"{car.registration_number:<12} | "
          f"{car.max_speed:<6} km/h | "
          f"{car.current_speed:<7} km/h | "
          f"{car.travelled_distance:.1f} km")