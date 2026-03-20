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
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered
test_car = Car("ABC-123", 142)
test_car.travelled_distance = 2000
test_car.current_speed = 60

test_car.drive(1.5)

print(f"Odometer after 1.5 hours of driving: {test_car.travelled_distance} km")