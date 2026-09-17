def factorial(n):

    if n == 0:

        return 1

    else:

        return n * factorial(n – 1)

number = int(input(“Nhập một số: “))

factorial_value = factorial(number)

print(“Giai thừa của”, number, “là:”, factorial_

