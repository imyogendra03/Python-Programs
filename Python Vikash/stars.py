'''# **********************************
print("*\n**\n***\n****\n",sep="")


#**********************************
n=int(input("Enter a number"))
for i in range(n):
    print("A",end="")
    for j in range(n):
        print("B",end="")
    print()'''


#  ****************  Pattern :3 ***************************

for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

    #*********************** Pattern 4 ***************************
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end="")
        else:
            print('',end="")
    print()