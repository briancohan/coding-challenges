from pathlib import Path
import logging
from itertools import batched
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


def parse_almanac(data: str) -> tuple[dict[int, int], dict[str, list[dict[str, int]]]]:
    keys = ["dest", "source", "length"]
    almanac = {}

    seeds, *data = data.strip().split("\n\n")
    seeds = {int(seed): int(seed) for seed in seeds.split(":")[1].split()}
    for chunk in data:
        name, spec = chunk.split(":")
        almanac[name.split()[0]] = [
            (dict(zip(keys, (map(int, line.split())))))
            for line in spec.strip().split("\n")
        ]

    return seeds, almanac


def get_location(
    seed: int,
    almanac: dict[str, list[dict[str, int]]],
) -> int:
    loc = seed
    for specs in almanac.values():
        for spec in specs:
            if spec["source"] <= loc <= spec["source"] + spec["length"]:
                loc = loc + spec["dest"] - spec["source"]
                break
    return loc


def get_min_location(
    pid: int,
    start: int,
    length: range,
    almanac: dict[str, list[dict[str, int]]],
    results_dict: dict[int, int],
) -> int:
    min_loc = 1e100
    for seed in range(start, start + length):
        loc = get_location(seed, almanac)
        if loc < min_loc:
            min_loc = loc
    results_dict[pid] = min_loc


def part_1(data: str) -> int:
    seeds, almanac = parse_almanac(data)

    for seed in seeds:
        seeds[seed] = get_location(seed, almanac)

    return min(seeds.values())


def part_2(data):
    seeds, almanac = parse_almanac(data)
    seeds = list(batched(seeds.keys(), 2))

    manager = multiprocessing.Manager()
    results = manager.dict()
    jobs = []

    for i, (start, length) in enumerate(seeds):
        p = multiprocessing.Process(
            target=get_min_location, args=(i, start, length, almanac, results)
        )
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    return min(results.values())


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text()

    print(part_1(data))
    print(part_2(data))
