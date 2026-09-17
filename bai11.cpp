def tinh_tong_so_chan(n):

    tong = 0

    for i in range(2, n+1, 2):

        tong += i

    return tong

# Thay đổi giá trị của n theo mong muốn

n = int(input("Nhập giá trị của n: "))

ket_qua = tinh_tong_so_chan(n)

print(f"Tổng của các số chẵn từ 1 đến {n} là: {ket_qua}")
