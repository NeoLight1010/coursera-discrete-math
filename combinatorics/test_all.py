from main import count_wins

def test_count_wins():
    assert count_wins([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == (15, 15)
    assert count_wins([1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9]) == (16, 20)
