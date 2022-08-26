













print("--------------------------A----------------------------------")

for row in range (0,6):
    for col in range (0,5):
        if ((col==0 or col==4 ) and row !=0)or (row==0 or row==3) and (col>0 and col<4):
            print("*", end="")
        else:
            print(end=" ")
    print()

print("--------------------------B----------------------------------")

for row in range (0,6):
    for col in range (0,4):
        if col==0 or (row==2  and (col!=3))or (row==0 and (col!=3))or (row==1 and(col!=1 and col!=2)) or (row==3 and(col!=1 and col!=2)) or (row==4 and (col!=1 and col!=2))or (row==5 and (col!=3)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()

print("--------------------------c----------------------------------")

for row in range(0,8):
    for col in range(0,4):
        if col==0 or row==0 or row==7:
            print("*" ,end=" ")
        else:
            print(end=" ")
    print()
    
print("--------------------------D----------------------------------")

for row in range(0,5):
    for col in range(0,4):
        if col==0 or (row==0 and (col!=3))or (row==4 and (col!=3))or (col==3 and (row>0 and row <4)):
            print("@", end="  ")
        else:
            print(end="  ")
    print()


print("------------------------------H---------------------------------")

for row in range (0,6):
    for col in range (0,5):
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
             print("*",end="")
        else:
            print(end=" ")

    print()



print("--------------------------------S-----------------------------------")
for row in range (0,6):
    for col in range (0,4):
        if row==0  or (row==3 and (col!=3))or row==5 or (col==0 and(row !=0 and row!=4)) or (col==3 and (row !=1 and row !=2 and row!=5)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()

print("----------------------------------------------------------------")
