from pathlib import Path

from aspose.zip.iso import IsoArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "archive.iso", "rb") as source:
        with IsoArchive(source) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressIso_out"))

    print("Successfully Opened Iso Archive")


if __name__ == "__main__":
    run()
