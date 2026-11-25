from pathlib import Path

from aspose.zip.saving import SevenZipEntrySettings, SevenZipLZMA2CompressionSettings
from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    archive_path = output_dir / "SolidArchive.7z"
    compression_settings = SevenZipLZMA2CompressionSettings()
    entry_settings = SevenZipEntrySettings(compression_settings, None)
    entry_settings.solid = True

    with SevenZipArchive(entry_settings) as archive:
        archive.create_entries(str(data_dir))
        archive.save(str(archive_path))

    print(f"Solid 7z archive created at: {archive_path}")


if __name__ == "__main__":
    run()
