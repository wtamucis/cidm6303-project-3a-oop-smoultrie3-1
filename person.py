# Create a simple class to represent a person
class Person():
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def set_age(self, age):
        try:
            if 0 < age < 120:
                self.age = age
            else:
                print("Please enter a valid age between 1 and 119.")
        except (ValueError, TypeError):
                print("Age must be a number between 1 and 119.")

    def speak(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old.")

p1 = Person("John", "Doe", 87)
p1.speak()

p2 = Person("Jane", "Smith", 56)
p2.speak()

p3 = Person("Anakin", "Skywalker", 25)
p3.speak()

p4 = Person("Luke", "Skywalker", 150)
p4.set_age("Hey")
print(p4.age)
p4.speak()
