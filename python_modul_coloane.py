bord = " "

def two_cols(lst, coldim):
    for x, y in lst:
        print(str(x) + bord + str(y))

def three_cols(lst, coldim):
    for x, y, z in lst:
        left_spaces = " " * ((coldim - len(x)) // 2)
        right_spaces = " " * ((coldim - len(x)) // 2)
        print(left_spaces + str(x) + right_spaces + bord + left_spaces + str(y) + right_spaces + bord + left_spaces + str(z) + right_spaces)


lst = [('1', '223'), ('5', '6'), ('5', '6')]
lst2 = [('1', '2', '3'), ('10', '5', '6')]
two_cols("str", 2)
two_cols(lst, 1)
two_cols(lst, 3)
three_cols(lst2, 22)
