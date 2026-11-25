from pathlib import Path

from aspose.zip import Archive
from CreateMultivolumeZip import run as create_multivolume_zip


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    create_multivolume_zip(output_dir)

    main_segment = output_dir / "MultivolumeArchive.zip"

    segments = [
        str(path)
        for path in sorted(output_dir.glob("MultivolumeArchive.z*"))
        if not path.name.endswith(".zip")
    ]

    with Archive(str(main_segment), segments) as archive:
        for entry in archive.entries:
            with open(output_dir / entry.name, "wb") as output:
                entry.extract(output)


if __name__ == "__main__":
    run()
