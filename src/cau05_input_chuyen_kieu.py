ma_may = input("Nhập mã máy: ")
cong_suat_w_str = input("Nhập công suất W: ")
so_phut_str = input("Nhập số phút: ")
don_gia_str = input("Nhập đơn giá: ")

print("\n--- Kiểu dữ liệu ngay sau khi nhập bằng input() ---")
print("ma_may:", type(ma_may))
print("cong_suat_w_str:", type(cong_suat_w_str))
print("so_phut_str:", type(so_phut_str))
print("don_gia_str:", type(don_gia_str))

cong_suat_w = float(cong_suat_w_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả sau khi chuyển kiểu và tính toán ---")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VND")