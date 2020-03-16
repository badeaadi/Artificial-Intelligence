fname = "fis.txt"
f = 0

class CustomError(IndexError):
    pass

try:
    f = open(fname, 'r')
except OSError:
    print("Could not open/read file:\n", fname)

try:
    x = 0
    list = [line.replace("\n","").split(" ") for line in f]
    l = len(list[0])
    for x in list:
        if len(x) != l:
            raise CustomError

    for x in list:
        x=[int(y) for y in x]
        print(x)


except ValueError:
    print("Some are not numbers\n")
except CustomError:
    print("Lines are not the same length")