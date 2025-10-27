
class SanPham:
    def __init__(self, ten_sp, gia, giam_gia):
        self.__ten_sp = ten_sp
        self.__gia = gia
        self.__giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.__gia * 0.1
    
    # getter/setter
    def get_ten_sp(self):
        return self.__ten_sp
    def set_ten_sp(self, ten_sp):
        self.__ten_sp = ten_sp
    # getter/setter của giá
    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia
    # getter/setter của giảm giá
    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia

    def nhap_thong_tin_san_pham(self):
        self.__ten_sp = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá sản phẩm (%): "))
    def xuat_thong_tin_san_pham(self):
        print(f"Tên sản phẩm: {self.__ten_sp}")
        print(f"Giá: {self.__gia}")
        print(f"Giảm giá: {self.__giam_gia}")
        print(f"Thuế thu nhập: {self.thue_nhap_khau()}")
    # kết quả trả về tương tự như xuat_thong_tin_san_pham nhưng code ngắn gọn hơn
    def __str__(self):
        return f"Sản phẩm {self.__ten_sp} có giá {self.__gia} giảm giá {self.__giam_gia} và thuế thu nhập {self.thue_nhap_khau()}"
    