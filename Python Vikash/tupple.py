t1=(34,43,5,4,3,4,45,45,43,23,22)    # this is tupple
print(t1)
  # type conversion or type casting
t2=list(t1)         #convert in list from tupple
print(t2)
t2.sort()   # sort() is to make assending order of give data

print(t2)
     

     #tuple can not be changable (append,replace,remove,pop,add)
     #tuple can store hetrogenious data

    #when we creat  function of tuple the use the function  :==  def fun(*k)
def fun(*k):        # tuple creation funcion
    print(k,type(k))
t=(32,23,43,54,65,67,87)