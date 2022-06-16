# class SinhVien:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def print_info(self):
#         print(self.name,self.age, self.gender)


# sv1 = SinhVien("anhnh",20, True)
# print(sv1.name)

# sv1.print_info()


class HocSinh:
    vidu = 1
    def __init__(self):
        print("Tôi là học sinh")
        self.name = "abc"

    # regular methods: phải truyền vào đối tượng là self


    @staticmethod
    def in_thong_tin_v2():
        print(test)

    @classmethod
    def in_thong_tin_v3(cls):
        cls.vidu +=1
    
    @classmethod
    def tao_object(cls):
        return cls()

    a = HocSinh.tao_object()

    
