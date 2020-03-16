l= ["bau-bau", "bobocel", "14 pisici", "1pitic", "pisicel", "botosel", "414", "ham", "-hau", "bob", "bocceluta"]

d_len={}


def create(d):
    d[(1,4)]="mic"
    d[(4,8)]="mediu"
    d[(8,15)]="mare"

create(d_len)
print(d_len)

d={}

def add_dict(d, l):

    for ch in set("".join(l)):
        d[ch] = []
        for word in l:
            if ch in word:
                d[ch].append(word)
    return d

add_dict(d, l)
print(d)


def delete_non(d):
    to_del=[]
    for ch in d:
        if not ch.isalpha():
            to_del.append(ch)
    for ch in to_del:
        del d[ch]


def count_keys(d):
    return len(d)


delete_non(d)
print(count_keys(d))


def print_types(d, d_len):
    for ch in d:
        types = set()
        for word in d[ch]:
            for limits in d_len:
                mn, mx = limits
                if(len(word) >= mn and len(word) <= mx):
                    types.add(d_len[limits])
        print(types)


print_types(d,d_len)