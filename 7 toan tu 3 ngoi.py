num_check = 4

# USING TERNARY OPERATOR
msg = "Even" if num_check %2 == 0 else "Odd"
print(msg)

# USING USUAL IF-ELSE
msg = ""
if(num_check%2  == 0):
    msg = "Even"
else:
    msg = "Odd"

print(msg)