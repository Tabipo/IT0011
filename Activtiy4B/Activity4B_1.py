setA = {"a", "b", "c", "d", "f", "g"}
setB = {"b", "c", "h", "l", "m", "o"}
setC = {"c", "d", "f", "h", "i", "j", "k"}

print("\nSets:")
print("Set A: ", setA)
print("Set B: ", setB)
print("Set C: ", setC)
print("")

union_AB = len(setA.union(setB))
print("Amount of Elements in set A and B:", union_AB)

unique_B = len(setB.difference(setA, setC))
print("Amount of Elements in set B but not in set A and C:", unique_B)

hijk = setC.difference(setA)
print(hijk)

cdf = setA.intersection(setC)
print(cdf)

B_inter_A = setB.intersection(setA)
B_inter_C = setB.intersection(setC)
bch = B_inter_A.union(B_inter_C)
print(bch)

A_inter_C = setA.intersection(setC)
df = A_inter_C.difference(setB)
print(df)

c = setB.intersection(setC, setA)
print(c)

lmo = setB.difference(setA, setC)
print(lmo)