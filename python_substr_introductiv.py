
str = (input("a."))
for i in range(0, len(str)):
    print(str[i :] + str[: i])

for i in range(0, len(str)):
    print(str[len(str) - i:] + str[:len(str) - i])

for i in range(1, len(str) // 2 + 1):
    print(str[: i] + '|' + str[len(str) - i : ])

