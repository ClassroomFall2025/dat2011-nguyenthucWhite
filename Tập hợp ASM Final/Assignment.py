# Viết ASM 1
# YÊU CẦU:
# Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.
# Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.
# Y3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.
# Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.
# Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.
# Y6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.
# Y7. Sắp xếp nhân viên theo họ và tên.
# Y8. Sắp xếp nhân viên theo thu nhập.
# Y9. Xuất 5 nhân viên có thu nhập cao nhất.

# • Final Assignment
# o Kiểm các lỗi dữ liệu nhập vào từ bàn phím
# o Hoàn thiện yêu cầu 1: lưu thông tin nhân viên vào file
# o Thực hiện yêu cầu 2: đọc thông tin nhân viên từ file, lưu vào danh sách và xuất ra màn hình
# o Thực hiện các yêu cầu 4 và 5.
import csv
import os

file_name = "danh_sach_nhan_vien.csv"

class NV:
    def __init__(self, ma, ho_ten, luong_co_ban):
        self.__ma_nv = ma
        self.__ho_ten = ho_ten
        self.__luong_co_ban = luong_co_ban
        self.loai_nv = "NV"

    def get_ma_nv(self):
        return self.__ma_nv
    def get_ho_ten(self):
        return self.__ho_ten
    def get_luong_co_ban(self):
        return self.__luong_co_ban
    
    def get_thu_nhap(self):
        return self.__luong_co_ban
    def get_thue_thu_nhap(self):
        thu_nhap = self.get_thu_nhap()
        if thu_nhap < 9000000:
            return 0
        elif thu_nhap <= 15000000:
            return thu_nhap * 0.10
        else:
            return thu_nhap * 0.12
    def xuat(self):
        print(f"NV,{self.get_ma_nv()},{self.get_ho_ten()},{self.get_luong_co_ban()},{self.get_thu_nhap()}")

class TT(NV):
    def __init__(self, ma, ho_ten, luong_co_ban, hoa_hong, doanh_so):
        super().__init__(ma, ho_ten, luong_co_ban)
        self.__hoa_hong = hoa_hong
        self.__doanh_so = doanh_so
        self.loai_nv = "TT"

    def get_hoa_hong(self):
        return self.__hoa_hong
    def get_doanh_so(self):
        return self.__doanh_so

    def get_thu_nhap(self):
        return self.get_luong_co_ban() + self.__hoa_hong * self.__doanh_so
    def xuat(self):
        print(f"TT,{self.get_ma_nv()},{self.get_ho_ten()},{self.get_luong_co_ban()},{self.__hoa_hong},{self.__doanh_so},{self.get_thu_nhap()}")

class TP(NV):
    def __init__(self, ma, ho_ten, luong_co_ban, luong_trach_nhiem):
        super().__init__(ma, ho_ten, luong_co_ban)
        self.__luong_trach_nhiem = luong_trach_nhiem
        self.loai_nv = "TP"

    def get_luong_trach_nhiem(self):
        return self.__luong_trach_nhiem
    def get_thu_nhap(self):
        return self.get_luong_co_ban() + self.__luong_trach_nhiem
    def xuat(self):
        print(f"TP,{self.get_ma_nv()},{self.get_ho_ten()},{self.get_luong_co_ban()},{self.__luong_trach_nhiem},{self.get_thu_nhap()}")

# Danh sách nhân viên
danh_sach_nv = []

def luu_file(ds_nv):
    """Ghi toàn bộ danh sách nhân viên vào file CSV, ghi đè nội dung cũ."""
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for nv in ds_nv:
            row = None
            if nv.loai_nv == "TT":
                row = [
                    "TT", 
                    nv.get_ma_nv(), 
                    nv.get_ho_ten(), 
                    nv.get_luong_co_ban(), 
                    nv.get_hoa_hong(), 
                    nv.get_doanh_so()
                ]
            elif nv.loai_nv == "TP":
                row = [
                    "TP", 
                    nv.get_ma_nv(), 
                    nv.get_ho_ten(), 
                    nv.get_luong_co_ban(), 
                    nv.get_luong_trach_nhiem()
                ]
            elif nv.loai_nv == "NV":
                row = [
                    "NV", 
                    nv.get_ma_nv(), 
                    nv.get_ho_ten(), 
                    nv.get_luong_co_ban()
                ]
            if row:
                writer.writerow(row)
    print(f"Đã lưu danh sách vào file {file_name}.")

def cn1():
    print("Chức năng 1: Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    so_luong_nv = int(input("Nhập số lượng nhân viên cần lưu:"))

    nv_moi_list = []
    for i in range(so_luong_nv):
        print(f"Nhập thông tin nhân viên thứ {i+1}:")
        vitri = input("Vị trí nhân viên (NV/TT/TP):").upper()
        ma = input("Mã nhân viên:")
        ho_ten = input("Họ tên nhân viên:")
        luong_co_ban = float(input("Lương cơ bản:"))

        if vitri == "NV":
            nv = NV(ma, ho_ten, luong_co_ban)
            nv.xuat()
        elif vitri == "TT":
            doanh_so = float(input("Doanh số bán hàng: "))
            hoa_hong = float(input("Tỉ lệ hoa hồng (%): ")) / 100
            nv = TT(ma, ho_ten, luong_co_ban, hoa_hong, doanh_so)
            nv.xuat()
        elif vitri == "TP":
            luong_trach_nhiem = float(input("Phụ cấp trách nhiệm: "))
            nv = TP(ma, ho_ten, luong_co_ban, luong_trach_nhiem)
            nv.xuat()
        else:
            print("Vị trí nhân viên không hợp lệ. Vui lòng nhập lại.")
            continue
        danh_sach_nv.append(nv)
        nv_moi_list.append(nv)

    print("Đã nhập xong danh sách nhân viên:")
    for nv in nv_moi_list:
        nv.xuat()    

    luu_file(danh_sach_nv)

def cn2():
    print("Chức năng 2: Đọc thông tin nhân viên từ file và xuất danh sách nhân viên")
    danh_sach_nv.clear()

    if not os.path.exists(file_name):
        print(f"File {file_name} không tồn tại. Vui lòng nhập nhân viên (CN1).")
        return
    
    with open(file_name, 'r', encoding='utf-8') as f:
        doc_thong_tin = csv.reader(f)
        for row in doc_thong_tin:
            if not row: # Bỏ qua dòng trống nếu có
                continue
            
            loai_nv = row[0]
            ma = row[1]
            ho_ten = row[2]
            luong_co_ban = float(row[3])
            
            nv = None
            if loai_nv == "NV":
                nv = NV(ma, ho_ten, luong_co_ban)
            elif loai_nv == "TT":
                hoa_hong = float(row[4])
                doanh_so = float(row[5])
                nv = TT(ma, ho_ten, luong_co_ban, hoa_hong, doanh_so)
            elif loai_nv == "TP":
                luong_trach_nhiem = float(row[4])
                nv = TP(ma, ho_ten, luong_co_ban, luong_trach_nhiem)
            
            if nv:
                danh_sach_nv.append(nv)
    
    print(f"Đã đọc {len(danh_sach_nv)} nhân viên từ file {file_name}:")
    if not danh_sach_nv:
        print("Danh sách rỗng.")
    else:
        for nv in danh_sach_nv:
            nv.xuat()

def cn3():
    print("Chức năng 3: Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.")
    ma = input("Nhập mã nhân viên cần tìm:")
    for nv in danh_sach_nv:
        if nv.get_ma_nv() == ma:
            print("Thông tin nhân viên:")
            nv.xuat()
            return
    print("Không tìm thấy nhân viên với mã đã nhập.")

def cn4():
    print("Chức năng 4: Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
    ma_xoa = input("Nhập mã nhân viên cần xóa: ")
    
    nv_can_xoa = None
    for nv in danh_sach_nv:
        if nv.get_ma_nv() == ma_xoa:
            nv_can_xoa = nv
            break
    
    if nv_can_xoa:
        danh_sach_nv.remove(nv_can_xoa)
        luu_file(danh_sach_nv) 
        print(f"Đã xóa nhân viên có mã {ma_xoa}.")
    else:
        print(f"Không tìm thấy nhân viên có mã {ma_xoa}.")

def cn5():
    print("Chức năng 5: Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.")
    ma_cap_nhat = input("Nhập mã nhân viên cần cập nhật: ")
    
    nv_can_cap_nhat = None
    index_nv = -1 
    
    for i in range(len(danh_sach_nv)):
        nv = danh_sach_nv[i]
        if nv.get_ma_nv() == ma_cap_nhat:
            nv_can_cap_nhat = nv
            index_nv = i 
            break 

    if nv_can_cap_nhat:
        print("Đã tìm thấy nhân viên. Vui lòng nhập thông tin mới (Giữ nguyên mã):")
        
        ho_ten_moi = input(f"Họ tên mới (hiện tại: {nv_can_cap_nhat.get_ho_ten()}): ")
        luong_moi = float(input(f"Lương cơ bản mới (hiện tại: {nv_can_cap_nhat.get_luong_co_ban()}): "))
        
        nv_moi = None
        
        if nv_can_cap_nhat.loai_nv == "TT":
            hoa_hong_moi = float(input(f"Tỉ lệ hoa hồng mới (%) (hiện tại: {nv_can_cap_nhat.get_hoa_hong()*100}): ")) / 100
            doanh_so_moi = float(input(f"Doanh số mới (hiện tại: {nv_can_cap_nhat.get_doanh_so()}): "))
            nv_moi = TT(ma_cap_nhat, ho_ten_moi, luong_moi, hoa_hong_moi, doanh_so_moi)
        
        elif nv_can_cap_nhat.loai_nv == "TP":
            luong_tn_moi = float(input(f"Lương trách nhiệm mới (hiện tại: {nv_can_cap_nhat.get_luong_trach_nhiem()}): "))
            nv_moi = TP(ma_cap_nhat, ho_ten_moi, luong_moi, luong_tn_moi)

        elif nv_can_cap_nhat.loai_nv == "NV":
            nv_moi = NV(ma_cap_nhat, ho_ten_moi, luong_moi)

        if index_nv != -1:
            danh_sach_nv[index_nv] = nv_moi
        
        # Lưu lại file
        luu_file(danh_sach_nv)
        print(f"Đã cập nhật thông tin cho nhân viên mã {ma_cap_nhat}.")

    else:
        print(f"Không tìm thấy nhân viên có mã {ma_cap_nhat}.")

def cn6():
    print("Chức năng 6: Tìm các nhân viên theo khoảng lương nhập từ bàn phím.")
    luong_min = float(input("Nhập mức lương tối thiểu: "))
    luong_max = float(input("Nhập mức lương tối đa: "))
    print(f"Các nhân viên có khoảng lương: {luong_min} - {luong_max}")
    for nv in danh_sach_nv:
        if luong_min <= nv.get_thu_nhap() <= luong_max:
            nv.xuat()

def cn7():
    print("Chức năng 7: Sắp xếp nhân viên theo họ và tên.")
    danh_sach_nv.sort(key=lambda nv: nv.get_ho_ten())
    for nv in danh_sach_nv:
        nv.xuat()

def cn8():
    print("Chức năng 8: Sắp xếp nhân viên theo thu nhập.")
    danh_sach_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    for nv in danh_sach_nv:
        nv.xuat()

def cn9():
    print("Chức năng 9: Xuất 5 nhân viên có thu nhập cao nhất.")
    danh_sach_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
    so_luong = min(5, len(danh_sach_nv))
    for nv in range(so_luong):
        danh_sach_nv[nv].xuat()

def cn10():
    print("Chức năng 10: Thoát chương trình.")
    print("Kết thúc chương trình.")