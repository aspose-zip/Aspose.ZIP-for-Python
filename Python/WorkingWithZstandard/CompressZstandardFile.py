from pathlib import Path

from aspose.zip.zstandard import ZstandardArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with ZstandardArchive() as archive:
        archive.set_source(str(data_dir / "alice29.txt"))
        archive.save(str(output_dir / "archive.zst"))

    print("Successfully Compressed a zstandard file")


if __name__ == "__main__":
    run()
