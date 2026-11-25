from pathlib import Path

from aspose.zip.tar import TarArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with TarArchive() as archive:
        archive.create_entry("alice29.txt", str(data_dir / "alice29.txt"))
        archive.create_entry("lcet10.txt", str(data_dir / "lcet10.txt"))
        archive.save_xz_compressed(str(output_dir / "archive.tar.xz"), None, None)


if __name__ == "__main__":
    run()
