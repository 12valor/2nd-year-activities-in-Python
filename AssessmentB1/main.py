def Voltage(a,b):
    volts = a * b
    return volts

a = int(input("ENTER CURRENT HERE: "))
b = int(input("ENTER RESISTANCE HERE: "))

print(Voltage(a,b), "volts")

for x in range(5):
    if x == 4:
        break

    else:
        print("hello")