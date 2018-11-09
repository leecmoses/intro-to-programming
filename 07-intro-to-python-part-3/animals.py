class Dog:
    scientific_name = "Canis lupus familiaris"  # class-level variable

    def __init__(self, name):  # instance-level variable (i.e. self.name)
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Yip!")

class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoooo!")