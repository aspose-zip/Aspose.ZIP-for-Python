from pathlib import Path

from aspose.zip.gzip import GzipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with GzipArchive() as archive:
        archive.set_source(str(data_dir / "data.bin"))
        archive.save(str(output_dir / "archive.gz"))

    print("Successfully Compressed a File")


if __name__ == "__main__":
    run()
