from pathlib import Path

from aspose.zip.lha import LhaArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "archive.lha", "rb") as source:
        with LhaArchive(source) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressLha_out"))


if __name__ == "__main__":
    run()
