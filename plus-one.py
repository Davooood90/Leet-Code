digits = [9]    

for i in range(len(digits) - 1, -1, -1):
    if digits[i] + 1 < 10:
        digits[i] += 1
        break
    else:
        digits[i] = 0

if digits[0] == 0:
    digits = [1] + digits

print(digits)