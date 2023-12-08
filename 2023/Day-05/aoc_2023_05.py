import multiprocessing
from itertools import batched
from pathlib import Path
from typing import NewType

Seed = NewType("Seed", dict[int, int])
Steps = NewType("Steps", dict[str, list[dict[str, int]]])
Data = NewType("Data", tuple[Seed, Steps])


def parse_input(full: bool = True) -> Data:
    input_file = Path(__file__).parent / ("input.txt" if full else "sample.txt")
    keys = ["dest", "source", "length"]
    steps = {}

    seeds, *data = input_file.read_text().strip().split("\n\n")
    seeds = {int(seed): int(seed) for seed in seeds.split(":")[1].split()}
    for chunk in data:
        name, spec = chunk.split(":")
        steps[name.split()[0]] = [
            (dict(zip(keys, (map(int, line.split())))))
            for line in spec.strip().split("\n")
        ]

    return seeds, steps


def get_location(seed: int, steps: Steps) -> int:
    loc = seed
    for specs in steps.values():
        for spec in specs:
            if spec["source"] <= loc <= spec["source"] + spec["length"]:
                loc = loc + spec["dest"] - spec["source"]
                break
    return loc


def get_min_location(
    pid: int,
    start: int,
    length: range,
    steps: Steps,
    results_dict: dict[int, int],
) -> int:
    min_loc = 1e100
    for seed in range(start, start + length):
        loc = get_location(seed, steps)
        if loc < min_loc:
            min_loc = loc
    results_dict[pid] = min_loc


def part_1(data: Data) -> int:
    seeds, steps = data

    for seed in seeds:
        seeds[seed] = get_location(seed, steps)

    return min(seeds.values())


def part_2(data: Data) -> int:
    seeds, steps = data

    manager = multiprocessing.Manager()
    results = manager.dict()

    jobs = [
        multiprocessing.Process(
            target=get_min_location, args=(i, start, length, steps, results)
        )
        for i, (start, length) in enumerate(batched(seeds.keys(), 2))
    ]

    for proc in jobs:
        proc.start()

    for proc in jobs:
        proc.join()

    return min(results.values())


if __name__ == "__main__":
    data = parse_input()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")
