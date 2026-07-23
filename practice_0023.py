# Practicing types and attributes:
class Human:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"{self.name} is talking.")
person = Human("Jacob")
print(person.name)
person.talk()
# Practicing functions:
class Plane:
    def takeoff(self):
        print("Plane is taking off...")
    def land(self):
        print("Plane is landing...")
plane = Plane()
plane.takeoff()
plane.land()