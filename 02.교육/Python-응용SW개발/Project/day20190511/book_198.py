# 아톰에서 한글처리시 반드시 포함해야 한다.
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class HousePark:
    lastname = '박'
    def __init__(self, name):
        self.fullname = self.lastname + name

    def setname(self, name):
        # self.lastname = '김'
        self.fullname = self.lastname + name    # local변수가 있음 먼저 적용된다.,

    def printInfo(self):
        print('full name :' , self.fullname)

    def travel(self, where):
        print('%s, %s 여행을 가다'%(self.fullname, where))

class HouseKim(HousePark):
    lastname = '김'

    def travel(self, where, day):
        print('%s, %s여을 %d일 가다'%(self.fullname, where, day))


# pey = HousePark()
# pes = HousePark()
#
# pey.setname('응용')
# pey.printInfo()
# pey.travel('부산')

pey = HousePark('보검')
pey.travel('부산')

j = HouseKim('줄리엣')
j.travel('독도', 10)
