print("Reading Student Information...")
fopen = open("students.txt", "r")
for line in fopen:
    print(line, end="")
fopen.close()