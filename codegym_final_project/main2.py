
def quan_ly_sach():
    print("""HOME\QUẢN LÝ SÁCH
Bấm phím để chọn yêu cầu thực hiện:
1: Liệt kê sách đang có - 2: Thêm sách mới - 3: Sửa thông tin sách - 4: Xóa thông tin sách - 0: Trở lại mục trước""")

    while True:
        user_input = input("Chọn yêu cầu: ")
        if user_input == '1':
            print("Danh sách đầu sách đang có")
        elif user_input == '2':
            print("Thêm sách mới")
        elif user_input == '3':
            print("Sửa thông tin sách")
        elif user_input == '4':
            print("Xóa thông tin sách")
        elif user_input == '0':
            break

def quan_ly_hoi_vien():
    print("HOME\QUẢN LÝ HỘI VIÊN")

def quan_ly_muon_sach():
    print("HOME\QUẢN LÝ MƯỢN SÁCH")

'''-----------------------------------------------------------------------------------------'''


print("""****************************************
*    CHƯƠNG TRÌNH QUẢN LÝ THƯ VIỆN     *
****************************************""")

while True:
    print("""HOME
Bấm phím để chọn yêu cầu thực hiện:
1: Quản lý sách - 2: Quản lý hội viên - 3: Quản lý mượn sách - 0: Thoát chương trình""")
    user_input = input("Chọn yêu cầu: ")
    if user_input == '1':
        quan_ly_sach()
    elif user_input == '2':
        quan_ly_hoi_vien()
    elif user_input == '3':
        quan_ly_muon_sach()
    elif user_input == '0':
        print("Goodbye!")
        break

