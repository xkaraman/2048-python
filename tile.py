EXP_MULTIPLIER = 2

class Tile:
    def __init__(self, value = 2 , upgradedThisMove = False):
        self.value = value
        self.upgradedThisMove = upgradedThisMove

    def upgrade(self):
        self.value *= EXP_MULTIPLIER
