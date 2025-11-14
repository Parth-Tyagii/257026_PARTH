#polymorphism-- same function name but diffrent behaivour
class cat:
    def speak(self):
        return "meow meow"
class dog:
    def speak(self):
        return "bow bow"
#polymorphism in action
def animal_sound(animal):
    print(animal.speak())