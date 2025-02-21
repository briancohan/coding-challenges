import json
import logging
from pathlib import Path
from typing import NewType
from collections import deque
import numpy as np
from PIL import Image
import cv2

Data = NewType("Data", list[str])

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    filename=Path(__file__).with_suffix(".log"),
    filemode="w",
)


def parse_input(full: bool = True, file_name: Path = None) -> Data:
    if file_name is None:
        file_name = "input.txt" if full else "sample.txt"
    input_file = Path(__file__).parent / file_name
    return input_file.read_text().strip().splitlines()


def locate_start(data: Data) -> tuple[int, int]:
    for i, row in enumerate(data):
        if "^" in row:
            return i, row.index("^")
    raise ValueError("Start not found")


def save_frame(data: Data, positions: list[tuple[int, int]]):
    img = np.zeros((len(data), len(data[0]), 3), dtype=np.uint8)

    for i in range(len(data)):
        for j in range(len(data[i])):
            img[i, j] = [255, 255, 255] if data[i][j] == "#" else [0, 0, 0]

    for i, j in positions[:-10]:
        img[i, j] = [0, 0, 125]
    for i, j in positions[-10:]:
        img[i, j] = [0, 0, 255]

    img[positions[0][0], positions[0][1]] = [0, 255, 0]
    img[positions[-1][0], positions[-1][1]] = [255, 0, 0]

    img = cv2.resize(
        img, (img.shape[1] * 10, img.shape[0] * 10), interpolation=cv2.INTER_NEAREST
    )

    filename = Path(__file__).parent / "frames" / f"frame_{len(positions):05d}.png"
    print(f"Writing {filename}")
    cv2.imwrite(filename, img)


def create_video():
    img = cv2.imread(str(Path(__file__).parent / "frames" / "frame_00002.png"))
    height, width, layers = img.shape
    files = sorted((Path(__file__).parent / "frames").glob("*.png"))

    video = cv2.VideoWriter(
        str(Path(__file__).parent / "animation.avi"),
        cv2.VideoWriter_fourcc(*"DIVX"),
        len(files) // (60 * 5),
        (width, height),
    )

    for file in files:
        print(f"stitching {file}")
        img = cv2.imread(file)
        video.write(img)

    cv2.destroyAllWindows()
    video.release()


def get_locations(data: Data) -> list[tuple[int, int]]:
    positions = [locate_start(data)]
    directions = deque([(-1, 0), (0, -1), (1, 0), (0, 1)])

    try:
        while True:
            next_pos = (
                positions[-1][0] + directions[0][0],
                positions[-1][1] + directions[0][1],
            )
            if min(next_pos) < 0:
                raise IndexError
            elif data[next_pos[0]][next_pos[1]] == "#":
                directions.rotate(1)
            else:
                positions.append(next_pos)
    except IndexError:
        pass

    return positions


def is_corner(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> bool:
    if p1[0] == p2[0] == p3[0] or p1[1] == p2[1] == p3[1]:
        return False

    return True


def part_1(data: Data) -> int:
    return len(set(get_locations(data)))


def part_2(data: Data) -> int:
    positions = get_locations(data)
    for pos in positions:
        logging.debug(pos)

    corners = [
        positions[ix]
        for ix in range(1, len(positions) - 1)
        if is_corner(positions[ix - 1], positions[ix], positions[ix + 1])
    ]
    for i, corner in enumerate(corners):
        logging.debug(f"Corner {i} at {corner}")

    return len(corners)


if __name__ == "__main__":
    data = parse_input(~False)

    # logging.debug(json.dumps(data, indent=4))

    for file in Path(__file__).parent.joinpath("frames").iterdir():
        file.unlink()

    # print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")
    # create_video()
