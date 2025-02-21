from pathlib import Path


def find_duplicate_item(packlist: str) -> str:
    mid = len(packlist) // 2
    item = set(packlist[:mid]).intersection(set(packlist[mid:]))
    return item.pop()


def get_item_priority(item: str) -> int:
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return ord(item) - 38


def score_packlist(packlists: list[str]) -> int:
    return sum(
        [get_item_priority(find_duplicate_item(packlist)) for packlist in packlists]
    )


def find_group_badge(group: list[str]) -> str:
    return (set(group[0]) & set(group[1]) & set(group[2])).pop()


def score_packlist_groups(packlists: list[str]) -> int:
    return sum(
        [
            get_item_priority(find_group_badge(group))
            for group in zip(*(iter(packlists),) * 3)
        ]
    )


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    packlists = input_file.read_text().split()

    print(score_packlist(packlists))

    print(score_packlist_groups(packlists))
