from pathlib import Path

from aspose.zip import Archive
from CompressMultipleFiles import run as compress_multiple_files


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    compress_multiple_files(output_dir)

    with Archive(str(output_dir / "CompressMultipleFiles_out.zip")) as archive:
        if len(archive.entries) > 0:
            archive.delete_entry(archive.entries[0])

        archive.save(str(output_dir / "rest_entries.zip"))


if __name__ == "__main__":
    run()
