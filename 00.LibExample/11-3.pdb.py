import pdb

def add(a, b):
    pdb.set_trace()
    return a+b

def main_call():
    return add(1,2)


if __name__=='__main__':
    r = main_call()
    print('a')
    print(r)