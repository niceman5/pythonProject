""" __call__함수는 클래스의 객체를 호출할수 있게 만드는 함수
"""

class CallMess:
    def __init__(self):
        self.mesg = "__call__ Test"
    def __call__(self):
        return self.mesg
    
class CallMess2:
    def __init__(self):
        self.mesg = "이메세지는 __call__ Test 새 메시지 입니다."
    def printMsg(self, user_mesg):
        um = self.mesg + user_mesg
        return um
    def __call__(self, user_mesg):
        return self.printMsg(user_mesg)
        
    
# 일반적인 방법으로 mesg호출
obj = CallMess()    
print(obj.mesg)

#하지만 __call__함수가 있는경우 클래스 객체를 호출하면 __call__값이 반환된다.
print(obj())



# 클래스 자체를 인스턴스 합수로 취급허고 변수를 넣어 사용하는 방법 
# 만약 클래스에 __call__ 메서드가 없으면 클래스를 인스턴스 함수처럼 사용할수 없고 호출 불가 오류가
# 뜸
obj2 = CallMess2()
print(obj2("아이고"))
