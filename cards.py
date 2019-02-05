class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"
c = Card("A", "hearts")
c1 = Card("10", "Diamonds")
c2 = Card("K", "Spades")

print(c,c1,c2)
