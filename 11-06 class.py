class SinhVien:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_info(self):
        print(self.name,self.age, self.gender)


sv1 = SinhVien("anhnh",20, True)
print(sv1.name)

sv1.print_info()


