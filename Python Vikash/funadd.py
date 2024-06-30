x=int(input("Enter first number"))
y=int(input("Enter second number"))
def add():                # function creation
    print("Addition is:",x+y)
def sub():                              #function creation
    print("Subtraction is:",x-y)
def mul():
    print("Multiplycation is:",x*y)
def div():
    print("Division is:",x/y)
def mod():
    print("Modulus is:",x%y)
add()           #function calling
sub()
mul()               #functon calling
div()
mod()


#       Actual and Formal parameter


def add(p,q):    # formal parameter      functon definition
    z=p+q
    print("Addition is:",z)
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
add(x,y)        #Actucal parameter    Function calling          




#    Actual and formal parameter using return function


def add(p,q):    # formal parameter      functon definition
    z=p+q
    return z
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
result=add(x,y)        #Actucal parameter    Function calling          
print("Adition is:",result)



