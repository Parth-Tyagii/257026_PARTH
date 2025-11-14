marks=[62,75,83,23,45,55,35,88,922,100]
for i in marks:
    if i>=35 and i<65:
        print("your grade is c")
    elif i>=65 and i<85: 
        print("your grade is b")
    elif i>=85 and i<95:
        print("your grade is a")
    elif i>=95:
        print("your grade is a++")
    else:
        print("fail...")             
