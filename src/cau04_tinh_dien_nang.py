cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

so_phut = 60
dien_nang_kwh_60 = cong_suat_w * so_phut / 60 / 1000
chi_phi_60 = dien_nang_kwh_60 * don_gia_kwh
print("\n[Khi số phút = 60]")
print("Điện năng (kWh):", dien_nang_kwh_60)
print("Chi phí (VND):", chi_phi_60)