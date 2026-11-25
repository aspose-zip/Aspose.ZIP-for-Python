from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveEntrySettings, ArchiveSaveOptions, StoreCompressionSettings


def run(output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "Data"
    output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "StoreMultipleFilesWithoutCompression_out.zip", "wb") as zip_file:
        file1 = data_dir / "alice29.txt"
        file2 = data_dir / "lcet10.txt"

        with Archive(ArchiveEntrySettings(StoreCompressionSettings())) as archive:
            archive.create_entry("alice29.txt", file1)
            archive.create_entry("lcet10.txt", file2)

            save_options = ArchiveSaveOptions()
            save_options.encoding = "ascii"

            archive.save(zip_file, save_options)


if __name__ == "__main__":
    example = Path(__file__).resolve()
    run(Path("Output") / example.parent.name / example.stem)
