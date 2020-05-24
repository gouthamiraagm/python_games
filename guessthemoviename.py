import random
movies=["anand","drishyam","nayakan""anbe sivam","goal mall","vickram veda","black friday","dangal","manichithara","taare"]
def paly():
    p1name=input("player1,please enter your name:")
    p2name=input("player2,please enter your name:")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        #alternate turn for two players (0,2,4,6,8....for player1) (1,3,5,,7,9 for player2)
        if turn%2==0:
            #player1
            print(p1name,"it is your turn")
            picked_movie=random.choice(movies)
            #create blanks here stars we are taken
            qn=create_question(picked)
            print qn
            modified_qn=qn
            not_said=true
            while not_said:
                letter=input("enter your letter: ")
                if(is_present(letter,picked-movie))
                #unlock the blank
                modified_qn=unlcok(modified_qn,picked_movie,ch)
                #(modified_qn,picked_movie) modified question from previous run
                #picked_movie for original reference
                #ch=changes to character 
                else:
                    print(letter,"not found")
            
            #player2
        else:
            turn=turn+1
             print(p2name,"it is your turn")
             
             
    
    
    
play()

