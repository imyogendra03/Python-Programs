# Swapcase()

# change small letter to capiltal letter or capital to small letter.

str = "This is Good Girl"
print(str.swapcase())

#count()

# count sub string under the substring
# count("substring",start,end)
print(str.count("is"))


# find()
# use for check position
# syntax also:- find("substr",start,end)

print(str.find("is"))

# index()

print(str.index('s'))

#rindex()

print(str.rindex('s'))

#join()

str1="john"
print("*".join(str1))

list=["first","second","third"]
print("**".join(list))

#split()

words=str.split(" ")
print(type(words))
print(words)

