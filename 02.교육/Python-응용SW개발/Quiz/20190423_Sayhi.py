
def say_hi(name:str, age:int) -> str:
    return "Hi. My name is {} and I'm {} years old".format(name, age)

##
# Main Process 처리
#
if __name__ == '__main__':
    print(say_hi('Alex',32))
    print(say_hi('Frank', 68))
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
    print(say_hi('Pepe', 8))