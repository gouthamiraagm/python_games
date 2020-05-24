end=100
from PIL import Image
import random 

def show_board():
    img=Image.open('C:\\Users\\Gouthami Ragam\\Desktop\\slb.JPG')
    img.show() 
def check_ladder(points):
    if points==8:
        print('ladder')
        return 26
    elif points==21:
        print('ladder')
        return 82
    elif points==43:
        print('ladder')
        return 77
    elif points==50:
        print('ladder')
        return 91
    elif points==54:
        print('ladder')
        return 93
    elif points==62:
        print('ladder')
        return 96
    elif points==66:
        print('ladder')
        return 87
    elif points==80:
        print('ladder')
        return 100
    else:
        #not a ladder
        return points #means no addition or incrementing the points
def check_snake(points):
    if points==44:
        print('snake')
        return 22
    elif points==46:
        print('snake')
        return 5
    elif points==48:
        print('snake')
        return 9
    elif points==52:
        print('snake')
        return 11
    elif points==55:
        print('snake')
        return 7
    elif points==59:
        print('snake')
        return 17
    elif points==64:
        print('snake')
        return 36
    elif points==69:
        print('snake')
        return 33
    elif points==73:
        print('snake')
        return 1
    elif points==83:
        print('snake')
        return 19
    elif points==92:
        print('snake')
        return 51
    elif points==95:
        print('snake')
        return 24
    elif points==98:
        print('snake')
        return 28
    else:
        #not a snake
        return points
def reached_end(points):
    if points==end:
        return True
    else:
        return False
        
def play():
    #input player1 name
    p1_name=input("player1,enter your name:")
    #input player2 name
    p2_name=input("player2,enter your name:")
    #intial points of palyer1 is zero
    pp1=0
    #intial points of palyer2 is zero
    pp2=0
    turn=0#we can intialze 1 also
    
    while(1):
        if turn%2==0:
            #player 1 turn
            print(p1_name,'your turn')
            #ask player's choice to continue
            choice=input("press 1 to continue, 0 to quit:")
            #if he wants quit show the score 
            if choice==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('quitting the game,thanks for playing')
                break
            #generate a random number fron 1,2 3,4 ,5 6
            #this is a simulation of rolling for a dice
            dice=random.randint(1,6)
            print('dice showed:',dice)
            #adding points to palyer
            pp1=pp1 + dice #it will give new update points
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            #check if the player goes beyond the board
            if pp1>end:
                pp1=end
            print(p1_name,'your score',pp1)
            
            if reached_end(pp1):
                print(p1_name,'won')
                break
        else:
            #player 2 turn
            print(p2_name,'your turn')
            #ask player's choice to continue
            choice=input("press 1 to continue, 0 to quit:")
            #if he wants quit show the score 
            if choice==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('quitting the game,thanks for playing')
                break
            #generate a random number fron 1,2 3,4 ,5 6
            #this is a simulation of rolling for a dice
            dice=random.randint(1,6)
            print('dice showed:',dice)
            #adding points to palyer
            pp2=pp2 + dice #it will give new update points
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            #check if the player goes beyond the board
            if pp2>end:
                pp2=end
            print(p2_name,'your score',pp2)
            
            if reached_end(pp2):
                print(p2_name,'won')
                break
        turn=turn+1
show_board()
play()
