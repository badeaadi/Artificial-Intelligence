
import sys

def parse_file(file_name):
    fin = open(file_name, "r")
    l = []
    n = 0
    for line in fin:
        str = line.replace(":", " ")
        str = str.replace("\n", "")
        print(str)
        word_list = str.split(' ')
        chair = int(word_list[0])
        while n < chair:
            l.append("gol")
            n += 1
        l.append(word_list[1])
    fin.close()
    return (l)

if __name__ == '__main__':
    print(parse_file("fis.txt"))
