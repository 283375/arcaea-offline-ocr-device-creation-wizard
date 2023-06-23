import argparse
import os
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument(
    "-no-obsolete",
    action="store_true",
    default=False,
    required=False,
    dest="no_obsolete",
)
args = ap.parse_args(sys.argv[1:])


script_file_path = Path(__file__)

root_dir_path = Path(script_file_path.parent.parent)
output_dir_path = Path(script_file_path.parent)

designer = root_dir_path / "designer"
extends = root_dir_path / "extends"
implements = root_dir_path / "implements"

assert designer.exists()
assert extends.exists()
assert implements.exists()

no_obsolete = args.no_obsolete

commands = [
    (
        "pyside6-lupdate"
        " -extensions py,ui"
        f" {extends.absolute()} {implements.absolute()}"
        f" -ts {str((output_dir_path / 'zh_CN.ts').absolute())}"
    ),  # zh_CN
    (
        "pyside6-lupdate"
        " -extensions py,ui"
        f" {designer.absolute()} {extends.absolute()} {implements.absolute()}"
        f" -ts {str((output_dir_path / 'en_US.ts').absolute())}"
    ),  # en_US
]
if no_obsolete:
    commands = [c + " -no-obsolete" for c in commands]

for command in commands:
    print(f"Executing '{command}'")
    output = os.popen(command).read()
    print(output)
