class Dog:
    scientific_name = "Canis lupus familiaris" #class-level variable

    def speak(self):
        print("Wolf!")
    
    def learn_name(self, name): #instance-level variable (i.e. self.name)
        self.name = name
    
    def hear(self, words):
        if self.name in words:
            self.speak()