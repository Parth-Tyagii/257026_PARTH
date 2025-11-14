#oops day 2
class car:
    def __init__(self, colour,model):#it works as an constructor...
        self.colour = colour#attribute
        self.model = model#attribute
        
    def driving(self):
        print(f"{self.colour} {self.model}is driving")
#object
car1=car("black","audi")
car2=car("grey","mustang")        

car1.driving()
car2.driving()


