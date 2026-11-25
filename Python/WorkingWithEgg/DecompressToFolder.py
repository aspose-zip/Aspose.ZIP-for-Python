from pathlib import Path

from aspose.zip.egg import EggArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "archive.egg", "rb") as source:
        with EggArchive(source) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressEgg_out"))


if __name__ == "__main__":
    run()
