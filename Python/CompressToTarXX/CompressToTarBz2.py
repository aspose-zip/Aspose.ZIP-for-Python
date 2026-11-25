from pathlib import Path

from aspose.zip.bzip2 import Bzip2Archive
from aspose.zip.tar import TarArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with Bzip2Archive() as bz2:
        with TarArchive() as archive:
            archive.create_entry("alice29.txt", str(data_dir / "alice29.txt"))
            archive.create_entry("lcet10.txt", str(data_dir / "lcet10.txt"))

            bz2.set_source(archive)
            bz2.save(str(output_dir / "archive.tar.bz2"))


if __name__ == "__main__":
    run()
