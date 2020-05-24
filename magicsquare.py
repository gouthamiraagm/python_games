def magic_square(n):
    #to define a matrix we need two loops
    magicsquare=[]#varible used as list
    for i in range(n):#it will go from 0 to 2
        l=[]#define a simple list evrey loop it will create a new list element
        for j in range(n):
            l.append(0)#here first it will check i value it is 0 then it creates an empty list
        magicsquare.append(l)#here we need append created l out of j loop and inside i loop
        #(i=n/2,j=n-1) number "1" location 
        #num=n*n(3*3=9)
        #count=1
    i=n//2
    j=n-1
    num=n*n
    count=1
    while (count<=num):
        if(i==-1 and j==n):#condition 4
            j=n-2
            i=0
        else:
            if(j==n):#coloumn value exceeding
                j=0
            if(i<0):#row becoming -1
            #here two if conditions means "or" one after other we will check
            #two conditions compulsary means and we will use
            #or condition is there means we can use twp if statements
                i=n-1
        #print (i, j, count, num, magicsquare)
        if (magicsquare[i][j]!=0):
            j=j-2#decrement coloum by 2
            i=i+1#increment coloum by 1
            continue #after doing this it may become like previous conditions so go back again upper loops and check
            #after continue statement it will skip down part and will go back to upper loop
        else:
            magicsquare[i][j]=count
            count=count+1
        i=i-1
        j=j+1#condition1
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=' ')
   
        print()
    print("the sum of each row/coloumn/diagonal is:"+str(n*(n**2+1)/2))
            
            
magic_square(3)
#l=[]   
#then it goes to j and it will take j=o
#and appned 0 to list now list becomes l=[0]
#next in that loop only it will take j=1
#and again append next 0 to list now the list is l=[0,0]  
#next in that loop it will take j=2
#and again it will append next 0 to the list now the list becomes l=[0,0,0]
#magicsquare.append(l)#here we need append created l=[0,0,0] after the j loop but it should be inside i loop
#once the j loop gets over it will append l to magicsquare that is our first row
#next it will take j=3 it is out of range so it will go the i 
#here now i become 1 so it is in range(3) so again it creates an empty list that is l=[]
#after that it goes to j take all j values that are 0 ,1,2 in every iteration it will append one zero to list
#now the list becomes l=[0,0,0] 
                      #l=[0,0,0]
        
    
