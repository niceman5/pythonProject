d = {'USA': 36, 'Germany': 17, 'France': 32}


def search_dict(word):
    c = dict((new_k.lower(), new_v) for new_k, new_v in d.items())
    print(c)
    return c.get(word, "찾을수 없음")


txt = input("Enter_Key :").lower()
print(txt)
print(search_dict(txt))