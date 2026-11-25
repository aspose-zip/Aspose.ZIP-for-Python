from pathlib import Path

from aspose.zip.lzma import LzmaArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with LzmaArchive() as archive:
        archive.set_source(str(data_dir / "alice29.txt"))
        archive.save(str(output_dir / "archive.lzma"))

    print("Successfully Compressed a File")


if __name__ == "__main__":
    run()
