tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
phut_con_lai = tong_phut % 60

print(f"Tổng thời gian: {so_gio} giờ và {phut_con_lai} phút")

bien_su_dung_lau = tong_phut > 60
print("Sử dụng trên 60 phút:", bien_su_dung_lau)

bien_du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", bien_du_lieu_hop_le)

# Dự đoán biểu thức:
# 100 + 20 * 3 -> Nhân trước, cộng sau -> 100 + 60 = 160
# (100 + 20) * 3 -> Ngoặc trước, nhân sau -> 120 * 3 = 360
print("Kết quả 100 + 20 * 3:", 100 + 20 * 3)
print("Kết quả (100 + 20) * 3:", (100 + 20) * 3)