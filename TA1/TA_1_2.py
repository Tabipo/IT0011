ctr = 0
sum = 0

numstr = input("Enter a string of digits: ")

for char in range(0, len(numstr)):
    sum += int(numstr[ctr])
    ctr += 1
print(sum)