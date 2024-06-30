#open(), write(), appent()
#write mode is also create new file
fp=open("a.txt","w")   # creat a file (a.txt)  and write in  the file
fp.write(input("Enter you data:"))

print(fp.name)
print(fp.mode)
print(fp.closed)
print(fp.readable)
print(fp.writable)
print(fp)
fp.closed()


# read mode is not creat new file
fp=open("a.txt","r")
print(fp.readline)
print(fp.readlines)


fp=open("a.txt","r")
while True:
    k=fp.readline()
    if k=='':
        break
    print(k,end="")
        

#append function is use to add some new data in the file

#w+,r+,a+ functon are also exist it is also work same as w,r,a function and some extra featurs
