from urllib.parse import parse_qs


# 넘겨받는 파라메터를 int로 구한다.
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default

    return found


# main test
p1 = parse_qs("red=50&blue=0&green", keep_blank_values=True)

red = get_first_int(p1, 'red')
blue = get_first_int(p1, "blue")
green = get_first_int(p1, "green")
black = get_first_int(p1, "black")
print("red: {} ".format(red))
print("blue: {} ".format(blue))
print("green: {} ".format(green))
print("black: {} ".format(black))

