age=int(input("Enter your age: "))
if age>10 and age<=18:
    print("You are a teenager.")
elif age>18:
    print("You are an adult.")
else:
    if  age<=10 and age>=0:
        print("You are a child.")
    else:
     print("Invalid age.")