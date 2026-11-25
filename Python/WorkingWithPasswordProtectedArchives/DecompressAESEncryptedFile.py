from pathlib import Path
from shutil import copyfileobj

from aspose.zip import Archive
from PasswordProtectWithAES import run as protect_with_aes


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    protect_with_aes(output_dir)

    with open(output_dir / "PasswordProtectWithAES256_out.zip", "rb") as source:
        with open(output_dir / "alice_aesextracted_out.txt", "wb") as extracted:
            with Archive(source) as archive:
                with archive.entries[0].open("p@s$") as decompressed:
                    copyfileobj(decompressed, extracted, length=8192)


if __name__ == "__main__":
    run()
