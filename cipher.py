import string
dict={}
data=""
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("C:\\Users\\Gouthami Ragam\\Desktop\\ip_file.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        print(data)   
        


import string
dict={}
data=""
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("C:\\Users\\Gouthami Ragam\\Desktop\\ip_file.txt") as f:
    while True:
        c=f.read(1)#here redaing by character by character,just supply a boolean variable 1
        if not c:
            print("end of file")#here we are checking that, did we encounter the end of file, if we reached the end of file then break it 
            break
        if c in dict:
            data=dict[c]#here presenting substitute values
        else:
            data=c #same letters
        file.write(data)
        print(data) 
file.close()
            
#keys are the letters present in the string and substitute letters are values      