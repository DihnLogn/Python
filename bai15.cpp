def kiem_tra_chuoi_con(chuoi_lon, chuoi_con):

    if chuoi_con in chuoi_lon:

        print(f’Chuỗi con “{chuoi_con}” tồn tại trong chuỗi “{chuoi_lon}”.’)

    else:

        print(f’Chuỗi con “{chuoi_con}” không tồn tại trong chuỗi “{chuoi_lon}”.’)

# Thay đổi các giá trị dưới đây để kiểm tra với các chuỗi cụ thể

chuoi_lon = “Chao mung ban den voi OpenAI”

chuoi_con = “ban”

kiem_tra_chuoi_con(chuoi_lon, chuoi_con)