print("Factorial Calculator")

num = int(input("Enter number: "))

if num < 0:
    print("Invalid input")
else:
    fact = 1
    i = 1
    
    while i <= num:
        fact = fact * i
        i = i + 1

    print("Factorial:", fact)

    if fact > 1000:
        print("Large factorial")
    else:
        print("Small factorial")

    print("Valid input")
