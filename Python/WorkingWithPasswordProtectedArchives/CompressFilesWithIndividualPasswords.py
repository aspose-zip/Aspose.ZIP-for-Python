from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import (
    ArchiveEntrySettings,
    DeflateCompressionSettings,
    TraditionalEncryptionSettings,
    AesEcryptionSettings,
    EncryptionMethod,
)


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    source1 = data_dir / "alice29.txt"
    source2 = data_dir / "asyoulik.txt"
    source3 = data_dir / "fields.c"

    settings1 = ArchiveEntrySettings(
        DeflateCompressionSettings(),
        TraditionalEncryptionSettings("pass1"),
    )
    settings2 = ArchiveEntrySettings(
        DeflateCompressionSettings(),
        AesEcryptionSettings("pass2", EncryptionMethod.AES128),
    )
    settings3 = ArchiveEntrySettings(
        DeflateCompressionSettings(),
        AesEcryptionSettings("pass3", EncryptionMethod.AES256),
    )

    with open(output_dir / "CompressFilesWithIndividualPasswords_out.zip", "wb") as zip_file:
        with Archive() as archive:
            archive.create_entry("alice29.txt", source1, True, settings1)
            archive.create_entry("asyoulik.txt", source2, True, settings2)
            archive.create_entry("fields.c", source3, True, settings3)
            archive.save(zip_file)


if __name__ == "__main__":
    run()
