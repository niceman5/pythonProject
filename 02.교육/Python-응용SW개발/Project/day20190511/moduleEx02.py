# import testModule
#
# print(testModule.value)
# testModule.show()
#
# a = testModule.Increment()
# a.printValue()

# from testModule import value
# from testModule import show
# from testModule import Increment

# from testModule import value, show, Increment
# # from testModule import *  위와 동일...
#
# print(value)
# show()
# a = Increment()
# a.printValue()

# # 파일을 읽어올때 파일을 읽어서 실행시키고 다음라인이 실행된다.
# import imsi.testModule as tm
# # import imsi.aaa
# from imsi import aaa
#
# # print(tm.value)
# # tm.show()
# # a =  tm.Increment()
# # a.printValue()
#
# tm.show()
# # imsi.aaa.aaa_show()
# aaa.aaa_show()
#

# from imsi import *  --> 이렇게는 안됨 패키지내 모든 모듈을 읽을수 없음
from imsi import *      # __init__.py를 만들어서 처리해야 함.


testModule.show()
aaa.aaa_show()
