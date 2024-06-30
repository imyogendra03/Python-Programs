# ********Indexing and Slice Operator********

#  [start:end:step]

# it is not include end index and it take by default of the step is 1.
# indexing always started at 0.

x="python"
print(x[2])
print(x[0:5])

# outpput is t &   pytho
# this is called sliceing in python

y="abcdefghijklmnopqrstuvwxyz"
print(y[0::2])   
# we can  also using slice operator print the string

print(y[0:27:1])
# it is called negative indexing


#reverse string
print(y[-1:-27:-1])


