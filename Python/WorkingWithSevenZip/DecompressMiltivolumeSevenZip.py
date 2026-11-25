from pathlib import Path

from aspose.zip.sevenzip import SevenZipArchive
from CreateMultivolumeSevenZipArchive import run as create_multivolume_archive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    create_multivolume_archive(output_dir)

    parts = [
        str(path)
        for path in sorted(output_dir.glob("MultivolumeArchive.7z.*"))
    ]

    with SevenZipArchive(parts) as archive:
        archive.extract_to_directory(str(output_dir))


if __name__ == "__main__":
    run()
