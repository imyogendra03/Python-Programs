#    Slicing Operator
h1=[34,43,3,45,68,67,89,45,67,76,78]
print(h1[2:6:1])               # h1[start:end:steps]
print(h1[:6:1])               # h1[start:end:steps]
print(h1[: :1])               # h1[start:end:steps]
print(h1[: :2])               # h1[start:end:steps]
print(h1[: :])               # h1[start:end:steps]


# Reverse slicing operator or negative indexing:

print(h1[len(h1):-len(h1)-1:-1])  # this is negative indexing & len() is use to find the length


a="Yogendra kumar"
print(a)
print(a[len(a): :-1])   # reveresed using slice operator


