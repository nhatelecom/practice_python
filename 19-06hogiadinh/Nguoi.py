# Để quản lý các hộ dân cư trong một khu phố, 
# người ta cần các thông tin sau: 
# Số thành viên trong gia đình, Số nhà, thông tin mỗi cá nhân trong gia đình.
# Với mỗi cá nhân, người ta quản lý các thông tin sau: 
# Họ tên, Tuổi, Nghề nghiệp, số chứng minh nhân dân(duy nhất cho mỗi người).

# Yêu cầu 1: 
#     Hãy xây dựng lớp Nguoi để quản lý thông tin của mỗi cá nhân.
# Yêu cầu 2: 
#     Xây dựng lớp HoGiaDinh để quản lý thông tin của từng hộ gia đình.
# Yêu cầu 2: 
#     Xây dựng lớp KhuPho để quản lý các thông tin của từng hộ gia đình.
# Yêu cầu 3: 
#     - Nhập n HoGiaDinh. (n nhập từ bàn phím)
#     - Hiển thị thông tin của các hộ trong khu phố.

class Nguoi:
    id_list = []
    def __init__(self):
        self.input_info()
        
    def input_info(self):
        self.name = input("Nhập họ tên: ")
        self.id = input("Nhập CMND: ")
        while self.id in self.id_list:
            self.id = input("Nhập lại CMND: ")
        Nguoi.id_list.append(self.id)
        self.age = input("Nhập tuổi: ")
        self.job = input("Nhập công việc: ")
    
    def output_info(self):
        print("Họ và Tên: "+ self.name,end="\t")
        print("CMND: "+ self.id,end="\t")
        print("Tuổi: "+ self.age,end="\t")
        print("Công việc: "+ self.job)