g=[11,13,13,12,45,65,43,23,34]
print(max(g))   # to find the maximum value in g
print(min(g))   #to find the minimum value of g
print(len(g))    # to find the length of g
print(id(g))     # to find the address of g
print(type(g))   # to find the data type



#****************************************************#
# Maximum or Minimum in two  numbers

p=int(input("Enter the first number"))
q=int(input("Enter the second number"))
if p>q:
    print(p,"is Greater")
elif p<q:
    print(q,"is Greater")
else:
    print("Both are equal")