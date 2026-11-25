from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import SplitArchiveSaveOptions


def run(output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "Data"
    output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    with Archive() as archive:
        archive.create_entry("alice29.txt", data_dir / "alice29.txt")
        archive.create_entry("lcet10.txt", data_dir / "lcet10.txt")
        archive.create_entry("sample.txt", data_dir / "sample.txt")

        save_options = SplitArchiveSaveOptions("MultivolumeArchive", 65536)
        save_options.encoding = "ascii"

        archive.save_split(str(output_dir), save_options)


if __name__ == "__main__":
    example = Path(__file__).resolve()
    run(Path("Output") / example.parent.name / example.stem)
