
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

k = 0
while k != 5:
    k = int(input("Meniu\n1.Prima diagonala\n2.a doua diagonala\n3.conturul\n4.Suma elementelor\n5.iesire\n"))
    if k == 1:
        for i in range(4):
            print(matrix[i][i], sep = ' ')
    elif k == 2:
        for i in range(4):
            print(matrix[i][3 - i], sep = ' ')
    elif k == 3:
        for i in range(4):
            print(matrix[i][1], sep = ' ')
        for i in range(3) + 1:
            print(matrix[1][i], sep = ' ')
        for i in range(3) + 1:
            print(matrix[i][3], sep = ' ')
        print(matrix[2][1], sep = ' ')
        print(matrix[1][1], sep = ' ')
    elif k == 4:
        s = 0
        for i in range(4):
            for j in range(4):
                s += matrix[i][j]
        print(s)
    else:
        break
