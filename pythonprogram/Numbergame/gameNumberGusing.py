import random
print('''
        /..........------START....-----....GAME--------.......------/
      ''')
ty="y"
while ty == "y":
    Cnumber=random.randrange(1,101)
    userInput=int(input("Enter the number-- : "))
    if userInput>Cnumber:
        print("Computer Number: ",Cnumber)
        print("your Number: ",userInput)
        print("your guess number is too high")
    elif Cnumber>userInput:
        print("Computer Number: ",Cnumber)
        print("your Number: ",userInput)
        print("your guess number is too Low")
    else:
        print("Computer Number: ",Cnumber)
        print("your Number: ",userInput)
        print("your guess Number is Equal")
    ty=input("Enter the Y for more play or N for stop the game ")