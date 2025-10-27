class SinhVienPoLy:
    # Khởi tạo các thuộc tính
    def __init__(self, ho_ten, nganh_hoc):
        self.__ho_ten = ho_ten
        self.__nganh_hoc = nganh_hoc
    # tính điểm
    def get_diem(self):
        pass
    # xếp học lực
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <= 10:
            hoc_luc = "Xuất sắc"
        elif self.get_diem() >= 8:
            hoc_luc = "Giỏi"
        elif self.get_diem() >= 7:
            hoc_luc = "Khá"
        elif self.get_diem() >= 5:
            hoc_luc = "Trung Bình"
        elif self.get_diem() >= 0:
            hoc_luc = "Chưa Đạt"
        else:
            print("Điểm không hợp lệ!")
        return hoc_luc
    # Xuất thông tin sinh viên
    def Xuat_danh_sach_sinh_vien(self):
        print(f"{self.__ho_ten}, {self.__nganh_hoc}, {self.get_diem()}, {self.get_hoc_luc()}")
    def __str__(self):
        return f"{self.__ho_ten}, {self.__nganh_hoc}, {self.get_diem()}, {self.get_hoc_luc()}"
    
class SinhVienIT(SinhVienPoLy):
    def __init__(self, ho_ten, nganh_hoc, diem_Java, diem_html, diem_css):
        super().__init__(ho_ten, nganh_hoc)
        self.__diem_Java = diem_Java
        self.__diem_html = diem_html
        self.__diem_css = diem_css
    def get_diem(self):
        return (self.__diem_Java * 2 + self.__diem_html + self.__diem_css) / 4
        
class SinhVienBiz(SinhVienPoLy):
    def __init__(self, ho_ten, nganh_hoc, diem_marketing, diem_sales):
        super().__init__(ho_ten, nganh_hoc)
        self.__diem_marketing = diem_marketing
        self.__diem_sales = diem_sales
    def get_diem(self):
        return (self.__diem_marketing * 2 + self.__diem_sales) / 3
