from pathlib import Path

from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "archive.7z", "wb") as seven_zip_file:
        with SevenZipArchive() as archive:
            archive.create_entry("data.bin", str(data_dir / "alice29.txt"))
            archive.save(seven_zip_file)

    print("Successfully Created a Seven Zip File with AES Encryption Settings")


if __name__ == "__main__":
    run()
