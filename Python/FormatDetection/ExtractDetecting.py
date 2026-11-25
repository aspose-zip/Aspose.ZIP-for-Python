from pathlib import Path

from aspose.zip import ArchiveFactory


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in data_dir.glob("archive.*"):
        with ArchiveFactory.get_archive(str(file)) as archive:
            archive.extract_to_directory(
                str(output_dir / f"{archive.format.name}_out")
            )
            print(f"File {file.name} proceeded successfully.")


if __name__ == "__main__":
    run()
