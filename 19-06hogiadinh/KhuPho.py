from HoGiaDinh import HoGiaDinh
class KhuPho:
    def __init__(self):
        self.number_of_family = 0
        self.name = None
        self.family_list = []
    
    def input_info(self):
        self.name = input("Nhập tên khu phố: ")
        while True:
            option = input("Bạn có muốn nhập thêm hộ gia đình (y/n)? ")
            if option == "y":
                ho_gia_dinh_moi = HoGiaDinh()
                ho_gia_dinh_moi.input_info()
                self.family_list.append(ho_gia_dinh_moi)
                self.number_of_family +=1
            elif option == "n":
                break
            else:
                continue
    
    def output_info(self):
        print("Khu phố: "+ self.name)
        for family in self.family_list:
            family.output_info()

a = KhuPho()
a.input_info()

print("Danh sách phu phố")
a.output_info()

