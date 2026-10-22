from datetime import datetime

ma_phien = input("Mã phiên: ")
ma_may = input("Mã máy: ")
cong_suat_w = float(input("Công suất thiết bị (W): "))
so_phut = int(input("Thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Đơn giá điện (VND/kWh): "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n--- THÔNG TIN GHI NHẬN SỬ DỤNG LAB ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")