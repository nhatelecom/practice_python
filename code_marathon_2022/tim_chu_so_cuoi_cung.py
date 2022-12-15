a = 10
fact = 1

for i in range(1, a+1):
    fact = fact * i

print(fact)
while True:
    last_digit = fact%10
    fact = int(fact/10)

    if last_digit != 0:
        break

return last_digit
print(last_digit)