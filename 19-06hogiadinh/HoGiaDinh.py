from sys import implementation
from Nguoi import Nguoi
class HoGiaDinh:
    def __init__(self):
        self.number_of_member = 0
        self.address = None
        self.member_list = []

    def input_info(self):
        self.address = input("Nhập địa chỉ hộ gia đình: ")
        while True:
            option = input("Bạn có muốn nhập thêm thành viên (y/n)?: ")
            if option == "y":
                nguoi_moi = Nguoi()
                self.member_list.append(nguoi_moi)
                self.number_of_member +=1
            elif option == "n":
                break
            else:
                continue

    def output_info(self):
        print("Hộ gia đình: "+self.address)
        for member in self.member_list:
            member.output_info()

a = HoGiaDinh()
a.input_info()
a.output_info()

b = HoGiaDinh()
b.input_info()
b.output_info()