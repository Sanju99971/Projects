import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
all=s1 + s2 + s3 + s4
length= int(input("Please Enter the lenght of the password:    "))
password="".join(random.sample(all, length))
print("Your Password is :" , password)
