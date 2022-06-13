a = [1, 3, 5, 9, 15, 12, 9, 35, 47, 9, 12]
b = []


for i in a:
    if a.count(i) > 2:
        b.append(i)


print(a)
print(b)
