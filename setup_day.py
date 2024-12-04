import argparse
from pathlib import Path
from datetime import datetime

base_dir = Path(__file__).parent
template_dir = base_dir / "tmpl"


def fix_date(s: str, year: int, day: int) -> str:
    return s.replace("yyyy", str(year)).replace("dd", f"{day:02}")


default_year = datetime.now().year
last_day = max(
    [int(d.name.split("-")[1]) for d in base_dir.joinpath(str(default_year)).iterdir()]
)

parser = argparse.ArgumentParser(description="Setup a new day for Advent of Code")
parser.add_argument(
    "--year", type=int, help="The year to setup for", default=default_year
)
parser.add_argument("--day", type=int, help="The day to setup", default=last_day + 1)
args = parser.parse_args()

challenge_dir = base_dir.joinpath(str(args.year), f"Day-{args.day:02}")
challenge_dir.mkdir(parents=True, exist_ok=True)

for file in template_dir.iterdir():
    if file.is_dir():
        continue

    dest = challenge_dir.joinpath(fix_date(file.name, year=args.year, day=args.day))
    dest.write_text(fix_date(file.read_text(), year=args.year, day=args.day))
