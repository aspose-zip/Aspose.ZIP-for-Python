from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveEntrySettings, PPMdCompressionSettings


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "lcet10.txt"
    size = file_path.stat().st_size

    with open(file_path, "rb") as source:
        with Archive(ArchiveEntrySettings(PPMdCompressionSettings())) as archive:
            entry = archive.create_entry("lcet10.txt", source)
            percent_ready = 0

            def on_progress(sender, e):
                nonlocal percent_ready

                percent = 100 * e.proceeded_bytes // size

                if percent > percent_ready:
                    print(f"{percent}% compressed")
                    percent_ready = percent

            if hasattr(entry, "compression_progressed"):
                entry.compression_progressed += on_progress
            archive.save(str(output_dir / "reported_out.zip"))

    print("Successfully Compressed a zip file with progress reporting")


if __name__ == "__main__":
    run()
