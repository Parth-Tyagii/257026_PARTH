#import random
#print("random no. between 1-10 issss",random.randint(1,1000000)


#import datetime

#today=datetime.date.today()
#print(today)


#import math
#print("power of 10^7",pow(10,7))
#print("the square root of 81",math.sqrt(81))
#print("value of pi ",math.pi)
#print("the ceil of 6.7",math.ceil(6.7))
#print("the floor value of 6.7",math.floor(6.7))

def number():
    import random
    t=random.randint(-100,100)
    if t>0:
        print("the number is: positive")
    else:
        print("the number is negative")
        
    if t%2==0:
        print("the number is even")
    else:
        print("the number is odd")
        
number()           
    
