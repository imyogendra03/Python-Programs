# eval is auto declear the datatype of give data
x=eval(input("Enter a data"))
print(x)


# multiple number take from the keyboard in a single line
x,y=input("Enter the first number:"),input("Enter the second number") 
print(x,y)


#split function use 
#split() is use to saperate the data and store in the form of list.

x,y,z=input("Enter a data:").split('/')
print(x,y,z)


# Next program
x=input("tell me about yourself")
y=x.split(' ')
print(y,type(y))


#Third program  using for loop  & split
x,y,z=[int(i) for i in input("Enter 3 numbers:").split()]
print(x,y,z,type(x))


#fourth program using e val function:
x,y,z=[eval(g) for g in input("Enter 3 data:").split()]
print(x,y,z)


#Fifth program using list()
t1=list([eval(g) for g in input("Enter the data:").split()])
print(t1,type(t1))

# tuple
t1=tuple([eval(g) for g in input("Enter the data:").split()])
print(t1,type(t1))