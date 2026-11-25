from pathlib import Path

from aspose.zip import Archive
from CompressSingleFile import run as compress_single_file


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    compress_single_file(output_dir)

    with open(output_dir / "CompressSingleFile_out.zip", "rb") as source:
        with Archive(source) as archive:
            entry = archive.entries[0]
            percent_ready = 0

            def on_progress(sender, e):
                nonlocal percent_ready

                percent = 100 * e.proceeded_bytes // entry.uncompressed_size

                if percent > percent_ready:
                    print(f"{percent}% decompressed")
                    percent_ready = percent

            if hasattr(entry, "extraction_progressed"):
                entry.extraction_progressed += on_progress
            entry.extract(str(output_dir / "alice_extracted_out.txt"))


if __name__ == "__main__":
    run()
