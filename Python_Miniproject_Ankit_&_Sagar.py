#print( '''**--- Miniproject :- COWS & BULLS GAME ---**

#      It's Features includes :-
#   1. Giving Scores.
#   2. Telling Number of chances taken by the player to complete game.
#   3. Re-start of the game withn one click.

#Made by :-
# 1. ANKIT - DAGAR    (2K18CSUN01053)
# 2. SAGAR - AGGARWAL (2K18CSUN01082)   ''')

#-----------------------------* CODE - STARTS *-----------------------------------------#

import random         #IMPORTING LIBRARY, Random to generate radom number

def player_section():   #PLAYER section, it contains players all movements,
    while(True):                #from showing errors to giving drections
        try:
            global player_number
            z=player_number=input("Enter Your Number:- ")
            z=int(z)
            if(len(player_number)!=4):
                print("Kindly, enter a 4-digit number")
                continue
        except ValueError:
            print("The input you entered is not a number")
        else:
            x=0
            for i in range(0,4):
                x=x+player_number.count(player_number[i])
            if(x!=4):
                print("Digits can't be SAME !! enter a number with different digits")
                continue
            else:
                return

def random_number_section():  #This Section generates a Random number for the player.
    com_num=random.sample("0123456789",4)
    com_num="".join(com_num)
    return(com_num)

def Compare(a,b):    #This section Compares the Generated number with Players Given number
    a=str(a)
    b=str(b)
    for i in range(0,4):
        for j in range(0,4):
            if(i==j)and(a[i]==b[j]):
                global Bull
                Bull+=1
            elif(i!=j)and(a[i]==b[j]):
                global Cow
                Cow+=1
            else:
                pass

m=str(input("Enter Your Name:- "))
print("\n")
print("------****  WELCOME TO COWS AND BULLS GAME   ****------")
print('''RULES:-
    1. The number should have ONLY 4-digit with all different digits.
    2. When number's place value matches it will give as BULL.
    3. When number's place value didn't matches but that digit is present in actual number then,
    it will give as COW.''')
print("\n")

player_number=0
user_choice=True
while(user_choice):
    Cow=0
    Bull=0
    game_number=random_number_section()
    score=0
    while(True):
        player_section()
        score=score+1
        Compare(game_number,player_number)
        if(Bull==4):
            print("\n")
            print(" CONGRATS!!! ",m)
            print("\n")
            
            print("You have completed the game in ",str(score),"chances.")
            m1=(1000/(score))
            
            print("Your Score is ",m1)
            print("\n")
            print("Do you want to play again ?")
            print("Enter \"y\"to PLAY AGAIN.")
            print("Otherwise, enter anything to EXIT.")
            
            choice=input("Enter your choice:- ")
            if(choice=="y"):
                user_choice=True
            else:
                user_choice=False
            
            break
        else:
            print("Cow :- ",Cow)
            print("Bull :- ",Bull)
            Cow=0
            Bull=0
