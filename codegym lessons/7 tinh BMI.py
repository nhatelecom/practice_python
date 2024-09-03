can_nang = float(input("Nhập cân nặng theo kilogam: "))
chieu_cao = float(input("Nhập chiều cao theo mét: "))

BMI = can_nang/(chieu_cao*chieu_cao)

print("BMI=",BMI)
if BMI < 16:
    print("Gầy cấp độ III")
elif BMI < 17:
    print("Gầy cấp độ II")
elif BMI < 18.5:
    print("Gầy cấp độ I")
elif BMI < 25:
    print("Thể trạng bình thường")
elif BMI < 30:
    print("Thừa cân")
elif BMI < 35:
    print("Béo phì cấp độ I")
elif BMI < 40:
    print("Béo cấp độ II")
else:
    print("Béo cấp độ III")

