number =  1
for num in range (2,number):
    if number % num == 0:
        print("not prime")
    elif number > 100:
        break
    else:
        number +=1
        print(number)

    
    