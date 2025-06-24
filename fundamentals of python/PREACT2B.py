total = 0
num = 1

while num < 10:
    if num == 7:
        break

    if num % 2 != 0:
        print(num)
        total = total + num
        num += 1
        continue

    num += 1

print("total:", total)
