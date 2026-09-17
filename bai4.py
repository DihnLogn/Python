number = int(input(“Nhập một số: “))

is_prime = True

for i in range(2, number):

    if number % i == 0:

        is_prime = False

        break

if is_prime:

    print(“Số là số nguyên tố”)

else:

    print(“Số không phải là số nguyên tố”)

