from main import count_wins, find_the_best_dice


def test_count_wins():
    assert count_wins([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == (15, 15)
    assert count_wins([1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9]) == (16, 20)


def test_find_the_best_dice():
    assert (
        find_the_best_dice([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]])
        == -1
    )

    assert (
        find_the_best_dice([[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]])
        == 2
    )

    assert (
        find_the_best_dice(
            [
                [3, 3, 3, 3, 3, 3],
                [6, 6, 2, 2, 2, 2],
                [4, 4, 4, 4, 0, 0],
                [5, 5, 5, 1, 1, 1],
            ]
        )
        == -1
    )
