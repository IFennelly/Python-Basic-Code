nominal = int(input("Enter nominal:"))


while nominal!=1: 
    if nominal % 2==0:
        nominal = nominal/2
        print (nominal)
    else: 
        nominal=(nominal*3)+1
        print(nominal)