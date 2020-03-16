
l = ["haha", "poc", "Poc", "POC", "haHA", "hei", "hey", "HahA", "poc", "Hei"]
dict = {}

for i in range(0, len(l)):
    if not l[i] in dict.keys():
        dict[l[i]] = 1
    else:
        dict[l[i]] += 1
print(dict)
