#first recursion program
def fun1():
    print("Hello",end='')
    fun1()

fun1()

#Addition  using recursion
def sum1(n):
    if n==1:
        return 1
    else:
        return n+sum1(n-1)
r=sum1(int(input("Enter the value:")))
print("Sum is:",r)

#Factorial function using recursion
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
while True:
    r=fact(int(input("Enter the value:")))
    print("Factorial is:",r)


#Addition of two numbers using lambda expresion
r=lambda a,b:a+b
x=int(input("Enter first number:"))
y=int(input("Enter Seconde number:"))
p=r(x,y)
print("Sum is",p)


# Greatest number find usion lambda expresion
r=lambda a,b:a if a>b else b
x=int(input("Enetr First number:"))
y=int(input("Enetr second number:"))
p=r(x,y)
print("Greater number is",p)


#factorial function using lambda expression
r=lambda n:1 if n==1 else n*r(n-1)
x=int(input("Enter first number:"))
p=r(x)
print("Factorial is",p)