class Book:
    book_id_list = []
    def __init__(self):
        # self.input_info()
        self.book_id = ''
        self.book_title = ''
        self.book_author = ''
        self.book_quantity = ''
        
    def input_info(self):
        self.book_id = input("Nhập ID sách: ")
        while self.book_id in self.book_id_list:
            self.book_id = input("Nhập lại ID sách: ")
        Book.book_id_list.append(self.book_id)
        self.book_title = input("Nhập tên sách: ")
        self.book_author = input("Nhập tên tác giả: ")
        self.book_quantity = input("Nhập số lượng: ")


    def output_info(self):
        print("ID: "+ self.book_id,end="\t")
        print("Tên sách: "+ self.book_title,end="\t\t")
        print("Tác giả: "+ self.book_author,end="\t\t")
        print("Số lượng: "+ self.book_quantity)

    def change_info(self):
        print("Thông tin hiện tại: ",end="")
        self.output_info()

        new_temp_name = input("Sửa tên sách (Enter để bỏ qua): ")
        if new_temp_name != '':
            self.book_title = new_temp_name
        new_temp_name = input("Sửa tên tác giả (Enter để bỏ qua): ")
        if new_temp_name != '':
            self.book_author = new_temp_name
        new_temp_name = input("Sửa số lượng (Enter để bỏ qua): ")
        if new_temp_name != '':
            self.book_quantity = new_temp_name

        print("Thông tin đã thay đổi: ",end="")
        self.output_info()