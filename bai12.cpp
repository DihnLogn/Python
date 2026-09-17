def is_prime(number):

    if number <= 1:

        return False

    for i in range(2, int(number**0.5) + 1):

        if number % i == 0:

            return False

    return True

# Nhập số từ người dùng

user_input = int(input(“Nhập một số: “))

# Kiểm tra xem số nhập từ người dùng có phải là số nguyên tố hay không

if is_prime(user_input):

    print(f”{user_input} là số nguyên tố.”)

else:

    print(f”{user_input} không là số nguyên tố.”)