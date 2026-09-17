def tim_so_chan_dau_tien(danh_sach):

    for so in danh_sach:

        if so % 2 == 0:

            return so

    return None  # Trả về None nếu không tìm thấy số chẵn nào trong danh sách

# Ví dụ sử dụng

danh_sach_so = [1, 3, 5, 8, 9, 10, 15]

so_chan_dau_tien = tim_so_chan_dau_tien(danh_sach_so)

if so_chan_dau_tien is not None:

    print(f”Số chẵn đầu tiên trong danh sách là: {so_chan_dau_tien}”)

else:

    print(“Không có số chẵn nào trong danh sách.”)