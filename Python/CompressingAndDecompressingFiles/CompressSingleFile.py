from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveEntrySettings


def run(output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "Data"
    output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "CompressSingleFile_out.zip", "wb") as zip_file:
        with open(data_dir / "alice29.txt", "rb") as source:
            with Archive(ArchiveEntrySettings()) as archive:
                archive.create_entry("alice29.txt", source)
                archive.save(zip_file)


if __name__ == "__main__":
    example = Path(__file__).resolve()
    run(Path("Output") / example.parent.name / example.stem)
