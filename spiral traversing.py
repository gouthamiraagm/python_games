import turtle
turtle.bgcolor("black")
seurat=turtle.Turtle()
width=5
height=7

dot_distance=25
seurat.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    seurat.color("white")
    '''
    k=index of starting row
    l=index of starting column
    m=number of rows
    n=number of coloumn
    a=matrix
    '''
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #printing the first row from the remaining rows
        for i in range(l, n): #keep row constant and traverse throgh the coloumn
            #print(a[k][i],end=" ") 
            seurat.forward(dot_distance)
        k=k+1  #row position increased
        f=1
        
            
#here row is fixed that is k 
#only coloumn will cahnge that is we assigned to i
            
            
        seurat.right(90)
            #printing the first coloumn from the remaining coloumn
        for i in range(k,m):
            #print(a[i][n-1],end=' ')
            seurat.forward(dot_distance)
        n=n-1
        
        seurat.right(90)   
        if(k<m):
                #printing the last row from from the remaining rows
            for i in range(n-1,l-1,-1):
                #print(a[m-1][i], end=" ")
                seurat.forward(dot_distance)     
            m=m-1
            
        seurat.right(90)    
        if(l<n):
                #printing the first coloumn
            for i in range(m-1,k-1,-1):
                #print(a[i][l],end=" ")
                seurat.forward(dot_distance) 
            l=l+1
            
'''            
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
'''    
    
    
spiral(20,20)
turtle.done()
        
                    
                    
            
                
            
            
    
    
    