# Program to check the given number is prime or not
# prime means only divisible by self and one
x=int(input("Enter a number:"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
        break
else:
    print("Prime")


# Program to print all prime numbers b/w the range:

p=int(input("Enter starting range:"))
q=int(input("Enter ending number:"))
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
             break
    else:
        print(x,end="")


#Program to print the sum of two numbers prime numbers which is the middle of the given range:

p=int(input("Enter starting range:"))
q=int(input("Enter ending number:"))
h=[]
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
             break
    else:
        print(x,end=" ")
        h.append(x)
print()
m=(len(h))//2
print(h[m]+h[m-1])