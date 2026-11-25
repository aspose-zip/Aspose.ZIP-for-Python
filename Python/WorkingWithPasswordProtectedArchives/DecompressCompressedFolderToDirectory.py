from pathlib import Path

from aspose.zip import Archive, ArchiveLoadOptions
from PasswordProtectDirectory import run as protect_directory


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    protect_directory(output_dir)

    load_options = ArchiveLoadOptions()
    load_options.decryption_password = "p@s$"

    with open(output_dir / "all_corpus_encrypted_out.zip", "rb") as zip_file:
        with Archive(zip_file, load_options) as archive:
            archive.extract_to_directory(
                str(output_dir / "all_corpus_decrypted")
            )


if __name__ == "__main__":
    run()
