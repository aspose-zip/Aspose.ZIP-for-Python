from pathlib import Path

from aspose.zip.alz import AlzArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "archive.alz", "rb") as source:
        with AlzArchive(source) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressAlz_out"))


if __name__ == "__main__":
    run()
