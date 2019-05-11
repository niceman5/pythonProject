# 전역변수
value = 10

# 그냥 함수
def show():
    print('run show()')
    # 해당파일에서 실행시 __name__은 main이 되고....
    # 다른 파일에서 실행일때는 해당 물리 파일명이 됨.
    # 이걸로 이게 어디서 실행되는건지 확인할때 사용한다.
    print('__name__ :', __name__)

class Increment:
    def printValue(self):
        self.num = 100
        print('num : ', self.num)



# 해당파일에 직접실행되는 경우애는 show실행 아니면 실행안한다.
# test등을 위해서 사용한다.
if __name__ == '__main__':
    show()
