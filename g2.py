path = "C:/textfile/demofile.txt"
entries = int(input("How many entries do you want: "))
formattedlines = []
formattedlines.insert(0, f"{'First Name':<12} {'Last Name':<12} {'Score':<6}")
for i in range(entries):
    print(f"Entries: {i+1}")
    first = input("Enter first name")
    last = input("Enter last name")
    score = int(input("Enter score"))
    formattedlines.append(f"{first:<12} {last:<12} {score:<6}")

with open(path, "a") as file:
    for line in formattedlines:
        file.write(line + "\n")

print("\nFile saved successfully!")