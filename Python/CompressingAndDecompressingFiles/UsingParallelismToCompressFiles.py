from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveSaveOptions, ParallelOptions, ParallelCompressionMode


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with Archive() as archive:
        archive.create_entry("alice29.txt", str(data_dir / "alice29.txt"))
        archive.create_entry("asyoulik.txt", str(data_dir / "asyoulik.txt"))

        parallel_options = ParallelOptions()
        parallel_options.parallel_compress_in_memory = ParallelCompressionMode.ALWAYS

        save_options = ArchiveSaveOptions()
        save_options.parallel_options = parallel_options
        save_options.encoding = "ascii"
        save_options.archive_comment = "There are two poems from Canterbury corpus"

        archive.save(
            str(output_dir / "UsingParallelismToCompressFiles_out.zip"),
            save_options
        )


if __name__ == "__main__":
    run()
