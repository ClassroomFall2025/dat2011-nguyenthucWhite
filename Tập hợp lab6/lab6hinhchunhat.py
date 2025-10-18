class ChuNhat:
    def __init__(self, ChieuDai, ChieuRong):
        self.__ChieuDai = ChieuDai
        self.__ChieuRong = ChieuRong
    
    def get_Chu_Vi(self):
        return (self.__ChieuDai + self.__ChieuRong) * 2
    def get_Dien_Tich(self):
        return self.__ChieuDai * self.__ChieuRong
    
    def Xuat(self):
        print(f"Hình chữ nhật")
        print(f"Chiều dài: {self.__ChieuDai}")
        print(f"Chiều rộng: {self.__ChieuRong}")
        print(f"Chu vi: {self.get_Chu_Vi()}")
        print(f"Diện tích: {self.get_Dien_Tich()}")
        print("-" * 30)
class Vuong(ChuNhat):
    def __init__(self, Canh):
        super().__init__(Canh, Canh) # "Canh" thứ 2 trong hàm __init__ dùng để gọi hàm tạo của ChuNhat và truyền canh cho cả ChieuDai và ChieuRong.
        self.__Canh = Canh

    def Xuat(self):
        print(f"Hình vuông")
        print(f"Cạnh: {self.__Canh}")
        print(f"Diện tích: {self.get_Dien_Tich()}")
        print(f"Chu vi: {self.get_Chu_Vi()}")
