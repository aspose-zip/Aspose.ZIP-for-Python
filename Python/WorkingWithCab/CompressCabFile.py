from pathlib import Path

from aspose.zip.cab import (
    CabArchive,
    CabEntrySettings,
    CabMsZipCompressionSettings,
    CabStoreCompressionSettings,
)


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    cab_output_path = output_dir / "ComposeCab_out.cab"
    single_file_path = data_dir / "alice29.txt"
    html_file_path = data_dir / "cp.html"

    # Default entries use MSZip compression.
    default_settings = CabEntrySettings(CabMsZipCompressionSettings())
    with CabArchive(default_settings) as archive:
        archive.create_entry("texts/alice.txt", str(single_file_path))

        # Store selected files without extra compression.
        stored_settings = CabEntrySettings(CabStoreCompressionSettings())
        archive.create_entry("texts/reference.html", str(html_file_path), stored_settings)

        archive.save(str(cab_output_path))

    print("CAB archive composed successfully.")


if __name__ == "__main__":
    run()
