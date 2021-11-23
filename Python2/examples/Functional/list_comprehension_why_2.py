seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(seznam)

seznam3 = []

for item in seznam:
    if item % 3 == 0:
        seznam3.append(item)

print(seznam3)

seznam3B = [item for item in seznam if item % 3 == 0]

print(seznam3B)
