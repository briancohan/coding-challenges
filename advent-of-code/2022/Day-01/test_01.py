import day01

test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_total_calories_by_elf():
    assert day01.get_max_calories(test_data) == 24000


def test_total_calories_by_top_three_elves():
    top_calories = day01.get_top_calories(test_data)
    assert top_calories == [24000, 11000, 10000]
    assert sum(top_calories) == 45000
