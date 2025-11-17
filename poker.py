import random

class Card:
    """扑克牌类"""
    # 花色：黑桃、红心、草花、方块
    SUITS = ['♠', '♥', '♣', '♦']
    SUIT_ORDER = {'♠': 0, '♥': 1, '♣': 2, '♦': 3}

    # 点数：A, 2-10, J, Q, K
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    RANK_ORDER = {rank: idx for idx, rank in enumerate(RANKS)}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"

    def __repr__(self):
        return self.__str__()


class Deck:
    """牌组类"""
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)

    def deal(self, num_players=4):
        """发牌给玩家"""
        players = [[] for _ in range(num_players)]
        for i, card in enumerate(self.cards):
            players[i % num_players].append(card)
        return players


def sort_hand(hand):
    """按照黑桃、红心、草花、方块的顺序和点数从小到大排列"""
    return sorted(hand, key=lambda card: (Card.SUIT_ORDER[card.suit], Card.RANK_ORDER[card.rank]))


def main():
    # 创建并洗牌
    deck = Deck()
    deck.shuffle()

    # 发牌给4个玩家
    players = deck.deal(4)

    # 对每个玩家的手牌排序并显示
    for i, hand in enumerate(players, 1):
        sorted_hand = sort_hand(hand)
        print(f"玩家 {i} 的手牌 (共{len(sorted_hand)}张):")
        print(' '.join(str(card) for card in sorted_hand))
        print()


if __name__ == "__main__":
    main()
