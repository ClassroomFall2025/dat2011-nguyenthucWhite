class SinhVien:
    # Các thuộc tính
    #ten_sinh_vien = ""
    #nam_sinh = ""
    #diem = ""

    # Các phương thức
    def __init__(self, ten, nam, diem):
        self.ten_sinh_vien = ten
        self.nam_sinh = nam
        self.diem = diem

    def xuat_thong_tin(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Điểm: {self.diem}")

#sv1 = SinhVien()
#sv1.them_sinh_vien("Nguyễn Văn A", 2000, 8.5)
#sv1.xuat_thong_tin()