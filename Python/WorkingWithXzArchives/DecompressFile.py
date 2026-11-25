from pathlib import Path

from aspose.zip.xz import XzArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with XzArchive(str(data_dir / "archive.xz")) as archive:
        with open(output_dir / "alice29_out.txt", "wb") as extracted:
            archive.extract(extracted)

    print("Successfully Opened xz Archive")


if __name__ == "__main__":
    run()
