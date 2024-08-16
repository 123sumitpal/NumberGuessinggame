import random
print('''
        ****\-------....----****Game********START****...------......../****
      
      ****/ Rock vs  paper  = Paper wins
            Rock vs  scissor  = Rock wins
            paper vs scissor = scissor wins/*****
      ''')
l=["rock","scissor","paper"]

while True:
    Ccount=0
    ucount=0     
    uc=int(input('''game can start again.......
                                        1.play yes
                                        2.No | Exit
        '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper
'''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice = random.choice(l)
            if Cchoice==uchoice:
                print("Computer choice: ",Cchoice)
                print("user Choice : ",uchoice)
                print("Game Draw")
                ucount=ucount+1
                Ccount=Ccount+1
            elif( uchoice=="rock" and Cchoice=="scissor") or(uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer choice: ",Cchoice)
                print("user Choice : ",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer choice: ",Cchoice)
                print("user Choice : ",uchoice)
                print("Computer win")
                Ccount=Ccount+1

        print("Final Score.......")
        if ucount==Ccount:
            print("final Game is Drow.....")
            print("User Score : ",ucount)
            print("Computer score : ", Ccount)
        elif ucount>Ccount:
            print("User can win the game...")
            print("User Score : ",ucount)
            print("Computer score : ", Ccount)
        else:
            print("Computer can win the game...")
            print("User Score : ",ucount)
            print("Computer score : ", Ccount)
    else:
        break