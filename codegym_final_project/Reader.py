class Reader:
    reader_id_list = []
    def __init__(self):
        # self.input_info()
        self.reader_id = ''
        self.reader_name = ''

        
    def input_info(self):
        self.reader_id = input("Nhập ID độc giả: ")
        while self.reader_id in self.reader_id_list:
            self.reader_id = input("ID trùng. Nhập lại ID độc giả: ")
        Reader.reader_id_list.append(self.reader_id)
        self.reader_name = input("Nhập tên độc giả: ")

    def output_info(self):
        print("ID: "+ self.reader_id,end="\t")
        print("Tên độc giả: "+ self.reader_name)

    def change_info(self):
        print("Thông tin hiện tại: ",end="")
        self.output_info()

        new_temp_name = input("Nhập tên mới (Enter để bỏ qua): ")
        if new_temp_name != '':
            self.reader_name = new_temp_name

        print("Thông tin đã thay đổi: ",end="")
        self.output_info()
