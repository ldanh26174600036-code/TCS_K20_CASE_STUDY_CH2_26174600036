ma_phien = input("Mã phiên: ")
ma_may = input("Máy: ")
cong_suat_w = float(input("Công suất (W): "))
so_phut = int(input("Số phút: "))
don_gia_kwh = float(input("Đơn giá: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- KẾT QUẢ ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh}")
print(f"Chi phí: {chi_phi}")