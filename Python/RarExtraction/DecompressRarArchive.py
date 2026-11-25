from pathlib import Path

from aspose.zip.rar import RarArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "plrabn12.rar", "rb") as source:
        with RarArchive(source) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressRar_out"))


if __name__ == "__main__":
    run()
