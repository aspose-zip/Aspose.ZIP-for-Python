from pathlib import Path
from shutil import copyfileobj

from aspose.zip import Archive, ArchiveLoadOptions
from CompressMultipleFiles import run as compress_multiple_files


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    compress_multiple_files(output_dir)

    entry_names = []
    percent_ready = 0

    def on_entry_listed(sender, e):
        entry_names.append(e.entry.name)

    def on_progress(sender, e):
        nonlocal percent_ready

        percent = 100 * e.proceeded_bytes // sender.uncompressed_size

        if percent > percent_ready:
            print(f"{percent}% decompressed")
            percent_ready = percent

    load_options = ArchiveLoadOptions()
    if hasattr(load_options, "entry_listed"):
        load_options.entry_listed = on_entry_listed
    if hasattr(load_options, "entry_extraction_progressed"):
        load_options.entry_extraction_progressed = on_progress

    with open(output_dir / "CompressMultipleFiles_out.zip", "rb") as zip_file:
        with Archive(zip_file, load_options) as archive:
            print("Entries are: " + ", ".join(entry_names))

            with open(output_dir / "alice_extracted_out.txt", "wb") as extracted:
                with archive.entries[0].open() as decompressed:
                    copyfileobj(decompressed, extracted, length=8192)

            percent_ready = 0
            archive.entries[1].extract(str(output_dir / "asyoulik_extracted_out.txt"))


if __name__ == "__main__":
    run()
