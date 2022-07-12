from Book import Book
from Reader import Reader

book_list = []  # Sách trong thư viện
reader_list = []  # Danh sách độc giả
borrow_list = [] # Danh sách mượn sách

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
            new_book.input_info()
            # Sách đầu tiên thì thêm vào. Sách tiếp theo thì sort theo ID
            if book_list == []:                         
                book_list.append(new_book)
            else:
                counter = 0
                for book in book_list:
                    if int(new_book.book_id) > int(book.book_id):
                        counter += 1
                book_list.insert(counter,new_book)
                for ele in book_list:
                    print(ele)
        elif user_input == '3':
            print("HOME\QUẢN LÝ SÁCH\SỬA THÔNG TIN SÁCH")
            id_sach_can_sua = input("Nhập ID sách cần sửa: ")
            found_book = False # =True nếu tìm thấy sách cần sửa không?
            for book in book_list:
                if book.book_id == id_sach_can_sua:
                    sach_can_sua = book
                    sach_can_sua.change_info()
                    found_book = True
                    break
            if not found_book:
                print("-> Không tìm thấy ID sách này")
        elif user_input == '4':
            print("HOME\QUẢN LÝ SÁCH\XÓA THÔNG TIN SÁCH")
            id_sach_can_xoa = input("Nhập ID sách cần xóa: ")
            found_book = False # =True nếu tìm ra sách cần xóa
            counter = 0     # Vị trí sách cần xóa
            for book in book_list:
                if book.book_id == id_sach_can_xoa:
                    found_book = True
                    break
                else:
                    counter += 1
            
            if found_book:
                print("-> Sách muốn xóa: ",end="")
                book_list[counter].output_info()
                del book_list[counter]
                del Book.book_id_list[counter]
                # book_list.remove(id_sach_can_xoa)
                # Book.book_id_list.remove(id_sach_can_xoa)
                print("-> Đã xóa sách này!")
                print("Hiện tại còn:")
                for element in book_list:
                    print(element,end=',')
                    print("\n")
                for element in Book.book_id_list:
                    print(element,end=',')
                    print("\n")
            else:
                print("-> Không tìm thấy sách có ID này")
        elif user_input == '0': # Thoát lên mục trên
            break

def quan_ly_hoi_vien():
    while True:
        print("""HOME\QUẢN LÝ HỘI VIÊN
    Bấm phím để chọn yêu cầu thực hiện:
    1: Liệt kê danh sách hội viên - 2: Thêm hội viên - 3: Sửa thông tin hội viên - 4: Xóa thông tin hội viên - 0: Trở lại mục trước""")
        user_input = input("Chọn yêu cầu: ")
        if user_input == '1':
            print("HOME\QUẢN LÝ SÁCH\LIỆT KÊ HỘI VIÊN:")
            print("---------------------------------------------------------------------------------------")
            for reader in reader_list:
                reader.output_info()
            print("---------------------------------------------------------------------------------------")
        elif user_input == '2':
            print("HOME\QUẢN LÝ SÁCH\THÊM HỘI VIÊN MỚI")
            new_reader = Reader()
            new_reader.input_info()
            # Hội viên đầu tiên thì thêm vào. Hội viên tiếp theo thì sort theo ID
            if reader_list == []:                         
                reader_list.append(new_reader)
            else:
                counter = 0
                for reader in reader_list:
                    if int(new_reader.reader_id) > int(reader.reader_id):
                        counter += 1
                reader_list.insert(counter,new_reader)
        elif user_input == '3':
            print("HOME\QUẢN LÝ SÁCH\SỬA THÔNG TIN HỘI VIÊN")
            id_can_sua = input("Nhập ID hội viên cần sửa: ")
            found_reader = False # =True nếu tìm thấy hội viên cần sửa
            for reader in reader_list:
                if reader.reader_id == id_can_sua:
                    reader_can_sua = reader
                    reader_can_sua.change_info()
                    found_reader = True
                    break
            if not found_reader:
                print("-> Không tìm thấy ID sách này")
        elif user_input == '4':
            print("HOME\QUẢN LÝ SÁCH\XÓA THÔNG TIN HỘI VIÊN")
            id_can_xoa = input("Nhập ID hội viên cần xóa: ")
            found_reader = False # =True nếu tìm ra sách cần xóa
            counter = 0     # Vị trí sách cần xóa
            for reader in reader_list:
                if reader.reader_id == id_can_xoa:
                    found_reader = True
                    break
                else:
                    counter += 1
            
            if found_reader:
                print("-> Hội viên muốn xóa: ",end="")
                reader_list[counter].output_info()
                del reader_list[counter]
                del Reader.reader_id_list[counter]
                print("-> Đã xóa hội viên này!")
            else:
                print("-> Không tìm thấy hội viên có ID này")
        elif user_input == '0': # Thoát lên mục trên
            break

def quan_ly_muon_sach():
    while True:
        print("""HOME\QUẢN LÝ MƯỢN SÁCH
    Bấm phím để chọn yêu cầu thực hiện:
    1: Danh sách người đang mượn sách 2: Thêm mượn sách - 3: Trả sách - 0: Trở lại mục trước""")
        user_input = input("Chọn yêu cầu: ")
        if user_input == '1':
            print("HOME\QUẢN LÝ MƯỢN SÁCH\DANH SÁCH NGƯỜI ĐANG MƯỢN SÁCH")
            print("---------------------------------------------------------------------------------------")
            print("Người mượn - Tên sách")
            for element in borrow_list:
                reader_id = element[0]
                book_id = element[1]
                reader_name = ''
                book_title = ''
                
                for reader in reader_list:
                    if reader.reader_id == reader_id:
                        reader_name = reader.reader_name
                for book in book_list:
                    if book.book_id == book_id:
                        book_title = book.book_title
                print(reader_name,"-",book_title,end="\n")
            print("---------------------------------------------------------------------------------------")
        elif user_input == '2':
            print("HOME\QUẢN LÝ MƯỢN SÁCH\BỔ SUNG LƯỢT MƯỢN SÁCH")

            id_reader_borrow = input("Nhập ID người mượn sách: ")
            found_reader = False # =True nếu ID hợp lệ
            for reader in reader_list:
                if reader.reader_id == id_reader_borrow:
                    found_reader = True
                    print("Người mượn: "+reader.reader_name)
                    break
            if not found_reader:
                print("->Không tìm thấy ID độc giả này.")
            else:
                id_book_borrow = input("Nhập ID sách cần mượn: ")
                found_book = False # =True nếu ID hợp lệ
                for book in book_list:
                    if book.book_id == id_book_borrow:
                        found_book = True
                        print("Sách mượn: "+book.book_title)
                        break
                if not found_book:
                    print("->Không tìm thấy ID sách này.")
                    break
            
            if found_reader and found_book:
                new_record = [id_reader_borrow,id_book_borrow]
                if new_record not in borrow_list:
                    borrow_list.append(new_record)
                    print("Đã thêm lượt mượn sách mới thành công.")
                else:
                    print("Đã tồn tại bản ghi mượn sách này")
        elif user_input == '3':
            print("HOME\QUẢN LÝ MƯỢN SÁCH\TRẢ SÁCH")

            id_reader_return = input("Nhập ID người trả sách: ")
            id_book_return = input("Nhập ID sách cần trả: ")
            return_record = [id_reader_return,id_book_return]

            if return_record not in borrow_list:
                print("Không có bản ghi mượn sách này.")
            else:
                print("Trả sách thành công")
                borrow_list.remove(return_record)

        elif user_input == '0':
            break
        # reader_id = input("")

'''-----------------------------------------------------------------------------------------'''

# Khởi tạo 1 số dữ liệu sách và hội viên để tiết kiệm thời gian nhập

book1 = Book()
book1.book_id = '1'
book1.book_title = 'Kính vạn hoa'
book1.book_author = 'Nguyễn Nhật Ánh'
book1.book_quantity = '50'

book3 = Book()
book3.book_id = '3'
book3.book_title = 'Doraemon'
book3.book_author = 'Fujiko F. Fujio'
book3.book_quantity = '60'

book5 = Book()
book5.book_id = '5'
book5.book_title = 'Tây Du Ký'
book5.book_author = 'Ngô Thừa Ân'
book5.book_quantity = '40'

book6 = Book()
book6.book_id = '6'
book6.book_title = 'Dragon Ball'
book6.book_author = 'Akira Toriyama'
book6.book_quantity = '100'

book7 = Book()
book7.book_id = '7'
book7.book_title = 'Mật Mã Da Vinci'
book7.book_author = 'Dan Brown'
book7.book_quantity = '90'


book_list.append(book1)
book_list.append(book3)
book_list.append(book5)
book_list.append(book6)
book_list.append(book7)
Book.book_id_list.append(book1.book_id)
Book.book_id_list.append(book3.book_id)
Book.book_id_list.append(book5.book_id)
Book.book_id_list.append(book6.book_id)
Book.book_id_list.append(book7.book_id)


reader1 = Reader()
reader1.reader_id = '1'
reader1.reader_name = 'Nguyễn Hoàng Ánh'

reader3 = Reader()
reader3.reader_id = '3'
reader3.reader_name = 'Đỗ Lệ Chi'

reader_list.append(reader1)
reader_list.append(reader3)
Reader.reader_id_list.append(reader1.reader_id)
Reader.reader_id_list.append(reader3.reader_id)

borrow_list = [['1','1'],['3','5'],['3','6']]

'''---CHƯƠNG TRÌNH CHÍNH Ở ĐÂY---'''
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