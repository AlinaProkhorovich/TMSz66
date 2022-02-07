def divisors(numb):
    for i in range(numb - 1, 1, -1):
        if (numb % i == 0):
            print(i)
    print(numb)

divisors(int(input("Enter number: ")))