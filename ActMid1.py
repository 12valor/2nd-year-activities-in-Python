path = "C:/textfile/demofile.txt"
try:
    file = open(path, "w")
    file.write("WE ARE S09")
    print("File updated successfully!")
finally:
    file.close()