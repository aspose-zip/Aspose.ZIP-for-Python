from pathlib import Path

from aspose.zip.cpio import CpioArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with CpioArchive() as archive:
        archive.create_entry("alice29.txt", str(data_dir / "alice29.txt"))
        archive.create_entry("lcet10.txt", str(data_dir / "lcet10.txt"))
        archive.save_gzipped(str(output_dir / "archive.cpio.gz"))


if __name__ == "__main__":
    run()
