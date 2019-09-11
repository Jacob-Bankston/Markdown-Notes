# Duplicate Numbers

nums = [1,2,7,2,3,8,7,2,3,2,2,2,7,3,4,5]

duplicates = 0
duplicate_numbers = []

for a in nums:
    counter = 0
    for b in nums:
        if a in duplicate_numbers:
            break
        elif a == b and counter == 0:
            counter = 1
        elif a == b and counter == 1:
            counter = 0
            duplicate_numbers.append(a)
            duplicates = duplicates + 1

print(duplicates)