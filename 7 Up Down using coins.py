#Rock Paper Scissor Game using Coins

import random
coins=50

print("         Welcome to the Game of 7 Up 7 Down! Double your coins everytime you win")

print("You have",coins,"initially")
while True:
    
    q=input("Do you want to play this game? (y/n) : ")
    
    if(q=='y'):
        how_many=int(input("How Many Coins do you want to Bet for?"))
        if(how_many>coins):
            print("Sorry you don't have enough coins to play")
        else:        
            start=input("Will the number be greater than 7,equal to 7 or lesser than 7? (g,e,l) : ")
            a=random.randint(1,6)
            print("First value: ",a)
            b=random.randint(1,6)
            print("Second value: ",b)
            c=a+b
            print("Your total value is ",c)
            if(start=='l'):
                if(c<7):
                    print("Congrats,You won! ")
                    coins=coins-how_many
                    coins=coins+(how_many*2)
                    print("Coins Left: ",coins)
                else:
                    coins=coins-how_many
                    print("Better luck next time!")
                    print("Coins Left: ",coins)
            if(start=='e'):
                if(c==7):
                    print("Congrats,You won! ")
                    coins=coins-how_many
                    coins=coins+(how_many*2)
                    print("Coins Left: ",coins)
                else:
                    coins=coins-how_many
                    print("Better luck next time!")
                    print("Coins Left: ",coins)
            if(start=='g'):
                
                if(c>7):
                    print("Congrats,You won! ")
                    coins=coins-how_many
                    coins=coins+(how_many*2)
                    print("Coins Left: ",coins)
                else:
                    coins=coins-how_many
                    print("Better luck next time! \n\n")
                    print("Coins Left: ",coins)
                    
    elif(q=='n'):
        print("Okay, Bye ")
        break
    
        
            
