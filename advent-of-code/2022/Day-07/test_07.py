from collections import defaultdict

import day07

sample_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_list_pop():
    l = [1, 2, 3]
    l.pop()
    assert l == [1, 2]


def test_getting_location_in_dict_from_list():
    expected = {
        "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296},
    }
    fs = day07.crawl_filesystem(sample_input)
    assert fs == expected


def test_tuple_equality_and_append():
    assert (1, 2) != [1, 2]
    i = (1, 2)
    i += (3,)
    assert i == (1, 2, 3)


def test_directory_sizes():
    expected = {
        "/": 48381165,
        "/a": 94853,
        "/a/e": 584,
        "/d": 24933642,
    }
    fs = day07.crawl_filesystem(sample_input)

    dir_sizes = defaultdict(int)
    day07.get_directory_sizes(fs, dir_sizes)
    assert dir_sizes == expected
