from pathlib import Path

from aspose.zip.lzip import LzipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with LzipArchive(str(data_dir / "archive.lz")) as archive:
        with open(output_dir / "alice29_out.txt", "wb") as extracted:
            archive.extract(extracted)

    print("Successfully Opened Lz Archive")


if __name__ == "__main__":
    run()
