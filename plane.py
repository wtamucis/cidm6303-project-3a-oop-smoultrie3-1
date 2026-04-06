# Code a class that describe planes following the instructions. 
# We are just simulating a simple plane. You can imagine 
# these methods could control a plane's functionality
class Plane():
    empty_weight = 1043
    wing_span = 13.1
    engines = 1
    make = "Cessna 350"
    model = "LC40-550FG"
    speed = 0

    def __init__(self, name):
        self.name = name
        self.speed = 0

    def throttle_engine(self, amount):
        self.speed += amount
        if self.speed < 0:
            self.speed = 0
        print(f"Speed is now {self.speed} mph.")

    def pitch(self, degrees):
        if degrees > 0:
            print("Up, up, and away!")
        elif degrees < 0:
            print("Going down!")
        else:
            print("Level flight.")

    def roll(self, degrees):
        if degrees > 0:
            print("Rolling to the right!")
        elif degrees < 0:
            print("Rolling to the left!")
        else:
            print("Straight and level.")

plane1 = Plane("King of the Sky")
print(plane1.name)
plane1.throttle_engine(10);
plane1.throttle_engine(50);
plane1.throttle_engine(100);
plane1.pitch(0.10);
plane1.pitch(0);
plane1.throttle_engine(-50);
plane1.roll(0.10);
plane1.roll(-0.10);
plane1.roll(0);

print("\n\n")

plane2 = Plane("The Red Baron")
plane2.empty_weight = 975
plane2.wing_span = 14
plane2.engines = 1
plane2.make = "customized Wright J-5 Whirlwind"
plane2.model = "Ryan Airlines custom built"
print(plane2.name)
print("Start in Las Vegas, NV")
plane2.throttle_engine(20);
plane2.throttle_engine(80);
plane2.throttle_engine(150);
plane2.pitch(0.20);
plane2.pitch(0);
plane2.throttle_engine(-50);
plane2.roll(-0.10);
plane2.roll(0.10);
plane2.roll(0);
plane2.pitch(-0.15);
plane2.throttle_engine(-150);
print(f"{plane2.name} has landed in New York, NY, safe and sound.")

