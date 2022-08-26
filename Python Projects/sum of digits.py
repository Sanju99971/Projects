#Sum of the digits of the number
n=int(input("Please Enter the Number:   "))
sum=0
while n>0:
    sum= sum+ n%10
    n=n//10
print("Sum of the digits of the Number is =", sum)
