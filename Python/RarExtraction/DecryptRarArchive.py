from pathlib import Path

from aspose.zip.rar import RarArchive, RarArchiveLoadOptions


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    load_options = RarArchiveLoadOptions()
    load_options.decryption_password = "p@s$"

    with open(data_dir / "encrypted.rar", "rb") as source:
        with RarArchive(source, load_options) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressRar_out"))


if __name__ == "__main__":
    run()
