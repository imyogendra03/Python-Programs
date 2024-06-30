#  ****************PATTERN-1. N*N ********************

n=int(input("Enter the number: "))
for i in range(n):                                  #Squair 
    for j in range(n):
        print("*",end=" ")
    print(" ") 


#  ****************PATTERN-2. N*N ********************
 
n=int(input("Enter the to get a triangle: "))
for i in range(n):                            
    for j in range(i+1):                          #Right triangle
        print("*",end=" ")
    print(" ") 

