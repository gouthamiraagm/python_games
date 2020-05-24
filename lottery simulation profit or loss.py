'''
import random
account=0
for i in range(7): #to play for 7 days
    bet=random.randint(1,10)
    print(bet)
    lucky_draw=random.randint(1,10)
    print(lucky_draw)
    
    if(bet==lucky_draw):
        account=account+900-100
    else:
        account=account-100
    print(account) 
    
import random
account=0
for i in range(30): #to play for 30 days
    bet=random.randint(1,10)
    #print(bet)
    lucky_draw=random.randint(1,10)
    #print(lucky_draw)
    
    if(bet==lucky_draw):
        account=account+900-100
    else:
        account=account-100
print(account) # printing amount at the end final amount

import random
account=0
for i in range(365): #to play for 30 days
    bet=random.randint(1,10)
    #print(bet)
    lucky_draw=random.randint(1,10)
    #print(lucky_draw)
    
    if(bet==lucky_draw):
        account=account+900-100
    else:
        account=account-100
print(account) # printing amount at the end final amount
   
'''
import random
import matplotlib.pyplot as plt
account=0
x=[] #x-axis
y=[] #y-axis
for i in range(365): #to play for 30 days
    x.append(i+1) #starts at day1 our i is zero so add 1 to it
    bet=random.randint(1,10)
    #print(bet)
    lucky_draw=random.randint(1,10)
    #print(lucky_draw)
    
    if(bet==lucky_draw):
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print(account) # printing amount at the end final amount
plt.plot(x,y)
plt.show()
   

