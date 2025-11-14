#inheritance in class
class Animal:
    def speak(self):
        print("animal speaks")
class cat(Animal):# this takes data from animal class
    def speak(self):
        print("meow meow")
cat= cat()#object of cat class
cat.speak()#calling speak method of cat class