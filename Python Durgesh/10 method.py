# some important method of string in python
x="abcdefghijklmnopqrstuvwxyz"
print("Length",len(x))

# for all captal letter usin upper function eg:
print(x.upper())

#similarly we can use lower function for all letter keep in lower letter

y="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(y.lower())

#using "title function" we can all string's first letter capital or upper letter 

print(x.title())


#startswith function using we can check for start function is given "object"

print(x.startwirh("ABC"))

#endswith function using we can check for end function is given "object"
print(x.endswith("program"))