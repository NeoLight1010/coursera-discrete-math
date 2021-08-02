from typing import List


def count_wins(dice1: List[int], dice2: List[int]):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    for i in dice1:
        for j in dice2:
            if i > j: dice1_wins += 1
            if j > i: dice2_wins += 1

    return (dice1_wins, dice2_wins)

def main():
    pass

if __name__ == "__main__":
    main()
