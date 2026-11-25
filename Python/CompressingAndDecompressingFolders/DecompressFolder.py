from pathlib import Path

from aspose.zip import Archive
from CompressDirectory import run as compress_directory


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    compress_directory(output_dir)

    with open(output_dir / "CompressDirectory_out.zip", "rb") as zip_file:
        with Archive(zip_file) as archive:
            archive.extract_to_directory(str(output_dir / "DecompressFolder_out"))


if __name__ == "__main__":
    run()
