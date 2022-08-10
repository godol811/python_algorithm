n = input()

m = list(n.upper())

k = list(set(m))

count = []

for member in k:
    count.append(m.count(member))



if count.count(max(count)) > 1:
    print("?")
else:
    maxIndex = count.index(max(count))
    print(k[maxIndex])

