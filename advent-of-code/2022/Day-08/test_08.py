import day08

sample_input = """
30373
25512
65332
33549
35390
"""


def test_visible_trees():
    visible = day08.visible_trees(sample_input)
    assert visible == 21


def test_scenic_score():
    score = day08.best_spot(sample_input)
    assert score == 8


def test_find_blocking_tree():
    trees = [3, 4, 5, 3, 7]
    height = 4
    pos = day08.trees_visible_in_direction(height, trees)
    assert pos == 1
