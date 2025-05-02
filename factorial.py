'''num=int(input("Enter a number"))
f=0
d=0
sum=0
while f<=5:
    d=f*num
    sum=d*f
    #print(d)
    f=f+1
    #sum=sum+d
print(f"Factorial of {sum} is :" ,sum)
'''




def fact(a):
    if a==1:
        return a
    else:
        return a*fact(a-1)
    pass
num=int(input("Enter a number"))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", fact(num))