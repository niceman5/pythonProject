

def frange(arg1, *args):

    if len(args) == 0:
        start , end , step = 0.0, float(arg1), 0.25
    elif len(args) == 1:
        start, end, step = float(arg1), float(args[0]), 0.25
    elif len(args) == 2:
        start, end, step = float(arg1), float(args[0]), float(args[1])
    L = []
    v = start
    if step > 0:
        while v < end:
            L.append( v )
            v += step
    elif step < 0:
        while v > end:
            L.append( v )
            v -= step

    return L

if __name__ == '__main__':
    l = frange(1.0, 5.0, 0.3)
    print((l))
