# Example 1: Print even numbers less than 15, but stop if number is 12

num = 1
total = 0

while num < 15:
    if num == 12:
        break

    if num % 2 == 0:
        print(num)
        total += num
        num += 1
        continue

    num += 1

print("Total of even numbers:", total)


# Example 2: Skip numbers divisible by 4, print the rest, stop at 9

number = 1

while number <= 10:
    if number % 4 == 0:
        number += 1
        continue

    if number == 9:
        break

    print(number)
    number += 1


# Example 3: Print "Hello TUPV!" if number divisible by 5, stop at 18

count = 1

while count <= 20:
    if count == 18:
        break

    if count % 5 == 0:
        print("Hello TUPV!")
        count += 1
        continue

    print("Count is:", count)
    count += 1


# Example 4: Print numbers from 1 to 10, but skip even numbers

num = 1

while num <= 10:
    if num % 2 == 0:
        num += 1
        continue

    print(num)
    num += 1


# Example 5: Print multiples of 3, stop if the number is 15

num = 1

while num <= 20:
    if num == 15:
        break

    if num % 3 == 0:
        print(num)
    num += 1


# Example 6: Count down from 10, but skip odd numbers

num = 10

while num >= 1:
    if num % 2 != 0:
        num -= 1
        continue

    print(num)
    num -= 1


# Example 7: Sum odd numbers up to 20

num = 1
total_sum = 0

while num <= 20:
    if num % 2 != 0:
        total_sum += num
    num += 1

print("Total sum of odd numbers:", total_sum)


# Example 8: Print "TUP Visayas" for every 4th number, break at 16

num = 1

while num <= 20:
    if num == 16:
        break

    if num % 4 == 0:
        print("TUP Visayas")

    num += 1
