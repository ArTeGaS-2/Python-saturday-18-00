def reverse(b):
    l = []
    for i in range(0, len(b)):
        l.insert(0, b[i])
    return l
d = input("input:")
for i in reverse(d):
    print(i)
