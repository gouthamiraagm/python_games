#import string
#print(string.ascii_letters)#we will get lowercase and uppercase letters
#output:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

#this is a string we need to conver string to list
#import string
#symbols=[]
#symbols=list(string.ascii_letters)#conversion of string to a list
#print(symbols)
#output=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import random
import string
symbols=[]
symbols=list(string.ascii_letters)
#generating two more lists
card1=[0]*5
card2=[0]*5#five symbols in each card
pos1=random.randint(0,4)
pos2=random.randint(0,4)
#print(pos1)
#print(pos2)
#pos1 and pos2 are sane symbol position in card1 and card2 respectively
samesymbol=random.choice(symbols)
#appending same symbol(alphabet) to card1 and card2
symbols.remove(samesymbol)
#remove that alphabet from the symbol
if(pos1==pos2):
   card1[pos1]=samesymbol
   card2[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1    
print(card1)  
print(card2)  
ch=input("spot the similar symbol")
if(ch==samesymbol):
       print("right")
else:
       print("try again")
        
    

