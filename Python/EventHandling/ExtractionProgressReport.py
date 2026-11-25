from pathlib import Path

from aspose.zip import Archive, ArchiveLoadOptions


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    def on_progress(sender, e):
        percent = 100 * e.proceeded_bytes // sender.uncompressed_size
        print(f"{percent}% extracted")

    load_options = ArchiveLoadOptions()
    if hasattr(load_options, "entry_extraction_progressed"):
        load_options.entry_extraction_progressed = on_progress

    with Archive(str(data_dir / "archive.zip"), load_options) as archive:
        archive.extract_to_directory(str(output_dir / "ReportingExtracion_out"))

    print("Successfully Extracted a zip file with progress reporting")


if __name__ == "__main__":
    run()
