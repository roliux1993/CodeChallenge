#  Two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7 


divisionArray = []

for x in range(0, 100 ):
         
    if (x%5==0) and (x%7!=0):
            divisionArray.append(str(x))

    print (','.join(divisionArray))




