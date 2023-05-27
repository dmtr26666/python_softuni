word = str(input())

vowels_count =0

for char in word:
    if char == "a":
        vowels_count += 1
    elif char == "e":
        vowels_count += 2
    elif char == "i":
        vowels_count += 3
    elif char == "o":
        vowels_count += 4
    elif char == "u":
        vowels_count += 5

print(vowels_count)