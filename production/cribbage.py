def parse_card(card_as_text):
    return Card(card_as_text[0])


class Card(object):
    def __init__(self, rank):
        super()
        self.rank = rank
