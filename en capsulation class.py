class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def talk(self):
        print(f"{self.name} is {self.__age} years old")
    
#object   
p1 = person("parth","45") 
print(p1.__age)#this will  raise an error 