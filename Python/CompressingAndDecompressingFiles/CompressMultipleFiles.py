from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveSaveOptions


def run(output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "Data"
    output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "CompressMultipleFiles_out.zip", "wb") as zip_file:
        with open(data_dir / "alice29.txt", "rb") as source1:
            with open(data_dir / "asyoulik.txt", "rb") as source2:
                with Archive() as archive:
                    archive.create_entry("alice29.txt", source1)
                    archive.create_entry("asyoulik.txt", source2)

                    save_options = ArchiveSaveOptions()
                    save_options.encoding = "ascii"
                    save_options.archive_comment = "There are two poems from Canterbury corpus"

                    archive.save(zip_file, save_options)


if __name__ == "__main__":
    example = Path(__file__).resolve()
    run(Path("Output") / example.parent.name / example.stem)
