

print("------------------------------------------------------------------------------")

for row in range (0,7):
     for col in range (0,7):
         if col==4 or col==6 or (col==2 and(row!=5 and row!=6))or (col==1 and (row!=2 and row!=4 and row!=5 and row!=6))or (col==3 and (row>2 and row<4)):
             print("@",end=" ")
         else:
             print(end="  ")
     print() 

print("------------------------------------------------------------------------------")




for row in range (0,7):
     for col in range (0,7):
         if row==0 or (col==4 and (row!=4 and row!=5))or (col==2 and(row!=1 and row!=2))or (col==3 and(row!=1 and row!=2 and row!=4 and row!=5)):
             print("@", end=" ")
         else:
             print(end="  ")
     print()
     

print("------------------------------------------------------------------------------")


for row in range (0,7):
     for col in range (0,7):
         if row==0 or col==4 or (col==1 and (row!=1))or (row==2 and (col>0 and col<5)):
             print("@", end="")
         else:
             print(end=" ")
     print()

print("------------------------------------------------------------------------------")






