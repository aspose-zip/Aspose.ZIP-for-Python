from pathlib import Path

from aspose.zip.iso import IsoArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with IsoArchive() as iso_archive:
        iso_archive.create_entry("alice.txt", str(data_dir / "alice29.txt"))
        iso_archive.save(str(output_dir / "archive_out.iso"))

    print("Successfully Compressed Iso File")


if __name__ == "__main__":
    run()
