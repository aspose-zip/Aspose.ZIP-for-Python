from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import AesEcryptionSettings, ArchiveEntrySettings, EncryptionMethod


def run(output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "Data"
    output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for method in (EncryptionMethod.AES128, EncryptionMethod.AES192, EncryptionMethod.AES256):
        settings = ArchiveEntrySettings(None, AesEcryptionSettings("p@s$", method))
        with open(output_dir / f"PasswordProtectWith{method.name}_out.zip", "wb") as zip_file:
            with open(data_dir / "alice29.txt", "rb") as source:
                with Archive(settings) as archive:
                    archive.create_entry("alice29.txt", source)
                    archive.save(zip_file)


if __name__ == "__main__":
    example = Path(__file__).resolve()
    run(Path("Output") / example.parent.name / example.stem)
