from pathlib import Path

from aspose.zip import Archive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    source_archive_path = data_dir / "archive.zip"
    file_to_append = data_dir / "ptt5"

    with Archive(str(source_archive_path)) as archive:
        archive.create_entry("ptt5", str(file_to_append))
        archive.save(str(output_dir / "archive_append.zip"))


if __name__ == "__main__":
    run()
