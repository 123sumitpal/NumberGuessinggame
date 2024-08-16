print('''
        /..............START.......... CALCULATER.............../
''')
ty= "y"
while ty=="y":


    print('''
        + ADD
        - SUBTRACT
        * MULTIPLY
        / DIVIDE '''
    )
    num1=int(input("enter the value :1  "))
    num2=int(input("enter the value :2  "))
    opr=input("enter the operater(+,-,*,/)  ")
    if opr=="+":
        print(num1+num2)
    elif opr=="-":
        print(num1-num2)
    elif opr=="*":
        print(num1*num2)
    elif opr=="/":
        print(num1/num2)
    else:
        print("invalid operater...")

    ty=input("enter the operation to want to more operation Y/N:  ")
