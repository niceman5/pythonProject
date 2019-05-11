class Card():
    card_info = {}  # class변수

    def __init__(self, number, kind):
        Card.card_info[number] = kind

    def print_card(self):
        for key, value in Card.card_info.items():
            print('card number : {}, card kind {}'.format(key, value))


c1 = Card(4, 'spade')
c2 = Card(1, 'king')
c3 = Card(2, 'diamond')
c1.print_card()
