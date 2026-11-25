from pathlib import Path

from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with SevenZipArchive() as archive:
        archive.create_entries(str(data_dir))
        archive.save(str(output_dir / "SevenZip.7z"))

    print("Successfully Created a Seven Zip File")


if __name__ == "__main__":
    run()
