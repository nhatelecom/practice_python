from Book import Book
from Reader import Reader

book_list = []  # Sách trong thư viện
reader_list = []  # Danh sách độc giả

def quan_ly_sach():
    while True:
        print("""HOME\QUẢN LÝ SÁCH
    Bấm phím để chọn yêu cầu thực hiện:
    1: Liệt kê sách đang có - 2: Thêm sách mới - 3: Sửa thông tin sách - 4: Xóa thông tin sách - 0: Trở lại mục trước""")
        user_input = input("Chọn yêu cầu: ")
        if user_input == '1':
            print("HOME\QUẢN LÝ SÁCH\LIỆT KÊ SÁCH:")
            print("---------------------------------------------------------------------------------------")
            for book in book_list:
                book.output_info()
            print("---------------------------------------------------------------------------------------")
        elif user_input == '2':
            print("HOME\QUẢN LÝ SÁCH\THÊM SÁCH MỚI")
            new_book = Book()
            # Sách đầu tiên thì thêm vào. Sách tiếp theo thì sort theo ID
            if book_list == []:                         
                book_list.append(new_book)
            else:
                counter = 0
                for book in book_list:
                    if int(new_book.book_id) > int(book.book_id):
                        counter += 1
                book_list.insert(counter,new_book)
        elif user_input == '3':
            print("HOME\QUẢN LÝ SÁCH\SỬA THÔNG TIN SÁCH")
            id_sach_can_sua = input("Nhập ID sách cần sửa: ")
            for book in book_list:
                if book.book_id == id_sach_can_sua:
                    sach_can_sua = book
                    sach_can_sua.change_info()
                    break
        elif user_input == '4':
            print("HOME\QUẢN LÝ SÁCH\XÓA THÔNG TIN SÁCH")
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

