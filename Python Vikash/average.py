# find the large no of addition or average to use tuple
# first convert tuple and then convert in list and then apply the process
#     For adition of any number
def add(*g):           #tuple
    print("Tuple is:",g)
    print("List is:",list(g))
    sum=0
    for i in range(len(g)):
        sum=sum+g[i]  
    print("Adition is:",sum)

add(12,12,43,54,34,43,54,76,87,56,34,23,4,65,76)


#     Find the Average of any number
def add(*g):           #tuple
    print("Tuple is:",g)    # to print the tuple value
    print("List is:",list(g))      #To print the list value
    sum=0
    for i in range(len(g)):      #loop
        sum=(sum+g[i])/len(g)        #average calculation in float
    print("Actual Average of the given numbers is:",sum)
    sum=int((sum+g[i])/len(g))          #Average calculation in int
    print("Aproximate Average of the given numbers is:",sum)


add(12,12,43,54,34,43,54,76,87,56,34,23,4,65,76)



