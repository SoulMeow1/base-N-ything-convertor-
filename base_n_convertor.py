print("This program converts numbers from any base-n to any base-n\n")

while True:

    bfrom = input("What base number are you converting from(base 2 to 36):")

    while True:     #error checking
        if bfrom.isdigit() == False:
            print("Invalid input.")
            bfrom = input("What base number are you converting from(base 2 to 36):")
            continue
    
        bfrom = int(bfrom);

        if bfrom < 2 or bfrom > 36:
            print("Invalid input.")
            bfrom = input("What base number are you converting from(base 2 to 36):")
            continue

        break

    print("This system uses 0,1,2,3,4...,8,9,A,B,C,D,E,...X,Y,Z")
    numfrom = input("Enter number here(alphanumerics only):")

    invalidstr = False

    while True:     #error checking
        for i in numfrom: #space is illegal
            if i.isspace() == True:
                invalidstr = True
                break
        
        if invalidstr == True:
            print("Invalid input.")
            print("This system uses 0,1,2,3,4...,8,9,A,B,C,D,E,...X,Y,Z")
            numfrom = input("Enter number here(alphanumerics only):")
            invalidstr = False
            continue

        if bfrom < 10: #make sure numfrom does not contain illegal numbers
            for i in numfrom:
                if int(i) > bfrom:
                    invalidstr = True
                    break
        
        else: #make sure numfrom does not contain illegal letters
            for i in numfrom:
                if i.isupper() == True:
                    print("if", ord(i), ">", bfrom+54)
                    if ord(i) > (bfrom + 54):
                        invalidstr = True
                        break

                elif i.islower() == True:
                    
                    if ord(i) > (bfrom + 86):
                        invalidstr = True
                        break

        if invalidstr == True:
            print("Invalid input.")
            print("This system uses 0,1,2,3,4...,8,9,A,B,C,D,E,...X,Y,Z")
            numfrom = input("Enter number here(alphanumerics only):")
            invalidstr = False
            continue

        break

    bto = input("what base number are you converting to:")

    while True:     #error checking
        if bto.isdigit() == False:
            print("Invalid input.")
            bto = input("What base number are you converting from(base 2 to 36):")
            continue
    
        bto = int(bto);

        if bto < 2 or bto > 36:
            print("Invalid input.")
            bto = input("What base number are you converting from(base 2 to 36):")
            continue

        break

    numfrom = numfrom[::-1]
    deci = 0
    j = 0

    for i in numfrom: #converting from base-n to decimal
        if(i.isdigit() == True):
            deci = deci + int(i)*(bfrom**j)

        elif(i.isupper() == True):
            deci = deci + (ord(i) - 55)*(bfrom**j)

        else: #i == lower case letter
            deci = deci + (ord(i) - 87)*(bfrom**j)

        j = j + 1

    numto = ""

    while(deci != 0): #converting from decimal to base-n
        r = deci % bto
        #print("r:",r)
        if(r < 10):
            numto = numto + str(r)

        else:
            r = r + 55
            numto = numto + chr(r)
            r = r - 55

        deci = deci - r
        deci = deci / bto
        deci = int(deci)

    numto = numto[::-1]
    
    print("final number:",numto)
                   
    if input("Would you like to convert another number?(y/n):") == 'n':
        break

