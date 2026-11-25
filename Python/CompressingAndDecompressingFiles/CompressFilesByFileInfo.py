from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveSaveOptions


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "CompressFilesByFileInfo_out.zip", "wb") as zip_file:
        file1 = data_dir / "alice29.txt"
        file2 = data_dir / "fields.c"

        with Archive() as archive:
            archive.create_entry("alice29.txt", file1)
            archive.create_entry("fields.c", file2)

            save_options = ArchiveSaveOptions()
            save_options.encoding = "ascii"

            archive.save(zip_file, save_options)


if __name__ == "__main__":
    run()
