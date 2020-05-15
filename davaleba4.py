a, b, c, d = input("Enter: "), input(
    "Enter: "), input("Enter: "), input("Enter: ")
array = []
array.append(a)
array.append(b)
array.append(c)
array.append(d)
for i in sorted(array, key=len, reverse=True):
    print(i)
