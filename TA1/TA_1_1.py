ctr_vowel = 0
ctr_consonant = 0
ctr_number = 0
ctr_otherchar = 0
ctr_space = 0

str = input("Enter a string: " )

for char in str:
    if char.lower() in 'aeiou':
        ctr_vowel += 1
    elif char.lower() in 'bcdfghjklmnpqrstvwxyz':
        ctr_consonant += 1
    elif char.isdigit():
        ctr_number += 1
    elif char.isspace():
        ctr_space += 1
    else:
        ctr_otherchar += 1

print("Vowels: ", ctr_vowel)
print("Consonants: ", ctr_consonant)
print("Numbers: ", ctr_number)
print("Spaces: ", ctr_space)
print("Other Characters: ", ctr_otherchar)
