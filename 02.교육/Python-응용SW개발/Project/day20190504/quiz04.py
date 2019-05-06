# class변수를 이용한다. 모든 인스턴스가 공유한다.

class Card():
    card_info = []
    def __init__(self, num, card_type):
        self.card_info.append([num, card_type])

    def print_card(self):
        for var in self.card_info:
            print('card number= {}, card_type : {}'.format(var[0], var[1]))


c1 = Card(4, 'spade')
c2 = Card(1, 'king')
c3 = Card(2, 'diamond')
c1.print_card()
