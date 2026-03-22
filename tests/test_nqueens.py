from bfrehb import n_queens_tree

def test_n_queens():
    # Test for n=4, which has 2 solutions
    solutions_4 = list(n_queens_tree(4))
    assert len(solutions_4) == 2
    assert [1, 3, 0, 2] in solutions_4
    assert [2, 0, 3, 1] in solutions_4

    # Test for n=5, which has 10 solutions
    solutions_5 = list(n_queens_tree(5))
    assert len(solutions_5) == 10

    # Test for n=6, which has 4 solutions
    solutions_6 = list(n_queens_tree(6))
    assert len(solutions_6) == 4

    # Test for n=8, which has 92 solutions
    solutions_8 = list(n_queens_tree(8))
    assert len(solutions_8) == 92