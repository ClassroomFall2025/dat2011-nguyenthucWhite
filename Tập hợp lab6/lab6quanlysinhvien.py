import lab6sinhvien as svpl

class QuanLySinhVien:
    #Khởi tạo danh sách sinh viên ban đầu rỗng
    def __init__(self):
        self.dssv = []

    #Phương thức nhập danh sách sinh viên
    def nhap_danh_sach_sinh_vien(self):
        while True:
            ho_ten_sv = input(f"Nhập họ tên sinh viên: ")
            nganh_hoc = input(f"Nhập ngành học sinh viên (it/biz): ")
            if nganh_hoc.lower() == "it":
                java = float(input("điểm java:"))
                html = float(input("điểm html:"))
                css = float(input("điểm css:"))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, java, html, css)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "biz":
                marketing = float(input("điểm marketing:"))
                sales = float(input("điểm sales:"))
                sv = svpl.SinhVienBiz(ho_ten_sv, nganh_hoc, marketing, sales)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "exit":
                print("kết thúc nhập tt sinh viên")
                break
            else:
                print("Nhập chưa đúng yêu cầu")
            return self.dssv
    def Xuat_danh_sach_sinh_vien(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng!")
        else:
            print(f'{"họ tên sinh viên"}, {"ngành học"}, {"điểm"}, {"học lực"}')
            for sv in self.dssv:
                sv.Xuat_danh_sach_sinh_vien()
    def Xuat_danh_sach_SV_gioi(self):
        pass
    def Xep_sep_danh_sach_SV(self):
        pass