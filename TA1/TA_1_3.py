a = int(input("Enter a number: "))

for i in range(1, a + 1):
    for k in range(a - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()
print("--------------------------------------------------------------")
b = [1, 3, 5, 6, 7]
l = 0

while l <= len(b) - 1:
    n = b[l]
    ctr = 0
    while ctr < n:
        print(n, end="")
        ctr += 1
    print()
    l += 1