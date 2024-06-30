'''# to check the given number is prime or not
num=int(input("Enter a number"))
if num>1:
   for i in range(2,(num//2)+1):
        if num%i==0:
           print("number is not pime")
           break
   else:
      print("number is prime")
else:
   print("number is not prime")
  

#Another method

num=int(input("Enter a number"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("not prime")
            break
    else:
        print("prime")
            



  #print all prime numbers between  1 to 100

for num in range(0,100):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num,end=" ")'''
            
#prime number check using function creation

'''def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            print("number is not prime")
            break
    else:
        print("number is prime")
is_prime(int(input("Enter a number to check prime or not")))



# prime number print using function

def prime(num1,num2):
    for num in range(num1,num2):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                print(num,end=" ")
prime(int(input("Enter the first number")),int(input("Enter the second number")))'''




# Prime numbers check using recursion
