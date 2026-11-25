from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveSaveOptions, SelfExtractorOptions


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    sfx_path = output_dir / "archive_sfx.exe"

    save_options = ArchiveSaveOptions()
    save_options.self_extractor_options = SelfExtractorOptions()

    with Archive() as archive:
        archive.create_entry("alice29.txt", str(data_dir / "alice29.txt"))
        archive.create_entry("lcet10.txt", str(data_dir / "lcet10.txt"))
        archive.save(str(sfx_path), save_options)


if __name__ == "__main__":
    run()
