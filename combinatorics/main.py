from typing import List
import itertools as it


def count_wins(dice1: List[int], dice2: List[int]):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in dice1:
        for j in dice2:
            if i > j:
                dice1_wins += 1
            if j > i:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices: List[List[int]]):
    assert all(len(dice) == 6 for dice in dices)

    winners = []
    for i, j in it.combinations(range(len(dices)), 2):
        wins_i, wins_j = count_wins(dices[i], dices[j])

        if wins_i > wins_j: winners.append(i)
        if wins_j > wins_i: winners.append(j)

    if len(set(winners)) == 1:
        return winners[0]

    return -1


def main():
    pass


if __name__ == "__main__":
    main()
