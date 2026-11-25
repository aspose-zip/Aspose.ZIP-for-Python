from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveEntrySettings, TraditionalEncryptionSettings


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    corpus = data_dir / "canterburycorpus"
    source1 = corpus / "alice29.txt"
    source2 = corpus / "asyoulik.txt"
    source3 = corpus / "fields.c"

    settings = ArchiveEntrySettings(None, TraditionalEncryptionSettings("p@s$"))
    with open(output_dir / "CompressMultipleFilesWithTraditionalEncryption_out.zip", "wb") as zip_file:
        with Archive(settings) as archive:
            archive.create_entry("alice29.txt", source1)
            archive.create_entry("asyoulik.txt", source2)
            archive.create_entry("fields.c", source3)
            archive.save(zip_file)


if __name__ == "__main__":
    run()
