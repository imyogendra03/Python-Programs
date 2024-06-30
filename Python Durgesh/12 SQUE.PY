content=input("enter your string:")
# convert to lower case
content=content.lower()

for i in range(97,123):
    count=0
    j=chr(i)
    for l in content:
        if j==1:
            count=count+1
    if count>0:
            print(j,":",count)
            