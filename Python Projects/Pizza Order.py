#Program to Order Pizza
order=input("Hello! Would you like to order a pizza?  'Yes' Or, 'NO'     ")
if order=='Yes':
    size=input("Please select Your Size: 'Large', 'Medium' ,or , 'Small'. ")
    bill=0
    if size=='Large':
        bill=30
        print(f"Large Pizza is of ${bill} ")
        
    elif size=='Medium':
        bill=23
        print(f"Medium Pizza is of ${bill}")
    else:
        bill=15
        print( f"Small Pizza is of ${bill}")
    Topings=input("Would you like to have some Extraa topings:  'Yes', Or, 'No'     ")
    if Topings=='Yes':
        print("Each topings are of $10")
        bill+=10
        print(f"Your total bill is ${bill}")
    else:
        print("Thanks, Your order is being ready.")

    Drinks=input("Would you like to have some drink?  'Yes', or , 'No'    ")
    if Drinks=='Yes':
        Brand= int(input('''Please select your favourite Brand:
                         for Pepsi Press      1
                         for Coke press       2
                         for Thumbs-up press  3       '''))
        if Brand==1:
                   print("Pepsi is of $7")
                   bill+=7
                   print(f"Your total  bill is ${bill}")
        elif Brand==2:
             print("Coke is of $6")
             bill+=6
             print(f"Your Total bill is ${bill}")
        else:
             print("Thumbs-up is of $9")
             bill+=9
             print(f"Your Total Bill is ${bill}")
    else:
        print("Pizza is boring without Drinks.")
        
else:
    print("Thanks for your time. Have a good day")
        
