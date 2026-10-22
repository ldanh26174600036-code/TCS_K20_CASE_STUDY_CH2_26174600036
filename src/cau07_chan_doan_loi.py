# Code đã được khắc phục các lỗi sau chẩn đoán:
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Sửa lỗi 1: Chuyển str sang float để thực hiện phép nhân/chia
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")  # Sửa lỗi 2 (Tên biến dien_nang -> dien_nang_kwh) và Sửa lỗi 3 (Thiếu dấu ')' ở cuối)

# ==========================================
# NHẬT KÝ CHẨN ĐOÁN VÀ SỬA LỖI (TRACEBACK LOG)
# ==========================================
# Lỗi 1: SyntaxError: unexpected EOF while parsing / invalid syntax
# - Tệp: cau07_chan_doan_loi.py, Dòng: 6
# - Nguyên nhân: Thiếu dấu đóng ngoặc ')' ở cuối dòng print(f"Điện năng: ...")

# Lỗi 2: NameError: name 'dien_nang' is not defined
# - Tệp: cau07_chan_doan_loi.py, Dòng: 6
# - Nguyên nhân: Dùng sai tên biến 'dien_nang' trong khi biến khai báo ở trên là 'dien_nang_kwh'

# Lỗi 3: TypeError: can't multiply sequence by non-int of type 'float'
# - Tệp: cau07_chan_doan_loi.py, Dòng: 4
# - Nguyên nhân: 'cong_suat_w' lấy từ input() có kiểu str, không thể nhân/chia trực tiếp với số nguyên/thực.