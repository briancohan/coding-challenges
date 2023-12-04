from pathlib import Path


def locate_start(stream: str, buffer_size: int) -> int:
    for i in range(len(stream)):
        buffer = stream[i : i + buffer_size]
        if len(set(buffer)) == buffer_size:
            return i + buffer_size


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    data = input_file.read_text().strip()

    print(locate_start(data, 4))
    print(locate_start(data, 14))
