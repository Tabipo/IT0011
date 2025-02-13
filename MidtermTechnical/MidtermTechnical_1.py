f=open("numbers.txt","r")
linenum = 1
line=f.readline()
while line.strip() != "":
    numbers = [int(i.strip()) for i in line.split(",") if i.strip().isdigit()]
    nsum = sum(numbers)

    if str(nsum) == str(nsum)[::-1]:
        print("Line {}: {} (sum {}) - Palindrome".format(linenum, numbers, nsum))
    else:
        print("Line {}: {} (sum {}) - Not a Palindrome".format(linenum, numbers, nsum))
    
    line=f.readline()
    linenum += 1
f.close()