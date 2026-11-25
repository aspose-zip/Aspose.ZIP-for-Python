from pathlib import Path

from aspose.zip.bzip2 import Bzip2Archive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with Bzip2Archive() as archive:
        archive.set_source(str(data_dir / "alice29.txt"))
        archive.save(str(output_dir / "archive.bz2"))

    print("Successfully Compressed a bzip2 file")


if __name__ == "__main__":
    run()
