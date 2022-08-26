#Random password generator
import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXZ"
num="0123456789"
symbol="[]{}()%$#@*&"
all=lower + upper + num + symbol
length=int(input("Enter the Length of password:   ")) 
password="".join(random.sample(all,length))
print("The password You Generated is:",password)
