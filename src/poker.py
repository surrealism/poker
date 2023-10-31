  def populate(self):         # 生成一副牌
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        self.add(Card(rank, suit))

  def shuffle(self):         # 洗牌
    import random
    random.shuffle(self.cards)   # 打乱牌的顺序

  def deal(self, hands, per_hand=13): # 将牌发给玩家，每人默认13张牌
    for rounds in range(per_hand):
      for hand in hands:
        if self.cards:
          top_card = self.cards[0]
          self.cards.remove(top_card)
          hand.add(top_card)
          # self.give(top_card,hand) #上两句可以用此句替换
        else:
          print('不能继续发牌了，牌已经发完了!')

if __name__ == "__main__":
  print('This is a module with classes for playing cards.')
  players = [Hand(), Hand(), Hand(), Hand()]
  poke1 = Poke()
  poke1.populate()       # 生成一副牌
  poke1.shuffle()        # 洗牌
  poke1.deal(players, 13)    # 发给每人13张牌
  n = 1
  for hand in players:
    print('牌手', n, end=':')
    print(hand)
    n = n + 1