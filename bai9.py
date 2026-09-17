def so_sanh_hai_so(a, b):

    if a > b:

        return f”{a} lớn hơn {b}”

    elif a < b:

        return f”{a} nhỏ hơn {b}”

    else:

        return f”{a} bằng {b}”

# Sử dụng hàm so_sanh_hai_so

so1 = float(input(“Nhập số thứ nhất: “))

so2 = float(input(“Nhập số thứ hai: “))

ket_qua = so_sanh_hai_so(so1, so2)

print(ket_qua)