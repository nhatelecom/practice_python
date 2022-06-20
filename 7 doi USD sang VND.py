# Bước 1: Nhập số tiền USD cần đổi
# Bước 2: Nhập tỉ giá USD/VND 
# Bước 3: Tính toán ra số tiền VND theo tỉ giá và số tiền USD nhập vào bên trên
# Bước 4: In ra kết quả

money_usd = float(input("Nhập số tiền USD cần đổi: "))
currency_ratio = float(input("Nhập tỉ giá USD/VND: "))
money_vnd = money_usd * currency_ratio
print("Số tiền VNĐ tương đương:", money_vnd, "VNĐ")