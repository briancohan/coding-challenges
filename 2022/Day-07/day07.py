from collections import defaultdict
from pathlib import Path


def set_cwd(fs: dict, fs_path: list) -> dict:
    cwd = fs
    for loc in fs_path:
        cwd = cwd[loc]
    return cwd


def crawl_filesystem(log: str) -> dict:
    fs = dict()
    fs_path = []
    cwd = set_cwd(fs, fs_path)

    for line in log.strip().splitlines():
        # Filesystem Navigation
        if line.startswith("$ cd"):
            new_loc = line.split()[-1]

            if new_loc == "/":
                fs_path = []
            elif new_loc == "..":
                fs_path.pop()
            else:
                fs_path.append(new_loc)

            cwd = set_cwd(fs, fs_path)

        # List Contents
        elif line.startswith("$ ls"):
            continue

        # Create Directory
        elif line.startswith("dir"):
            folder = line.split()[-1]

            if folder not in cwd:
                cwd[folder] = dict()

        # Create File
        else:
            size, file = line.split()
            cwd[file] = int(size)

    return fs


def get_directory_sizes(fs: dict, sizes: defaultdict, path: list[str] = ()) -> None:
    """Recursivly get the size of each directory in the filesystem.

    This leverages `sizes` which is a mutable input so that subsequent calls
    to this function can update the dictionary.
    """
    for key, value in fs.items():
        if isinstance(value, dict):
            get_directory_sizes(value, sizes, path + (key,))
        else:
            for i in range(len(path) + 1):
                pth = "/" + "/".join(path[:i])
                sizes[pth] += value


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    fs = crawl_filesystem(input_file.read_text())

    dir_sizes = defaultdict(int)
    get_directory_sizes(fs, dir_sizes)
    print(sum(size for size in dir_sizes.values() if size <= 100000))

    disk_space = 70000000
    update_size = 30000000
    used_space = dir_sizes["/"]
    free_space = disk_space - used_space
    need_to_clear = update_size - free_space

    print(min(size for size in dir_sizes.values() if size > need_to_clear))
