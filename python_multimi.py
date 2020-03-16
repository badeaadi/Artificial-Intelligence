def check_equals(number_list):
    return len(set(number_list)) == 1

my_list = [1, 1, 1]
print(check_equals(my_list))

def check_alphabet(word):
    return len(set(word.lower())) == 26

print(check_alphabet("abcdee"))

def check_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)


word1 = "abcdeee"
word2 = "badceee"
print(check_anagrams(word1, word2))


from itertools import chain, combinations

#d.
l = [1, 2, 3]
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list(powerset(l)))

somelists = [[1, 2, 3], [4, 5, 6]]
#e.
import itertools

for element in itertools.product(*somelists):
    print(element)