from pathlib import Path

from aspose.zip.xar import XarArchive, XarStoreCompressionSettings, XarZlibCompressionSettings


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    xar_output = output_dir / "ComposeXar_out.xar"
    text_file_path = data_dir / "alice29.txt"
    html_file_path = data_dir / "cp.html"
    directory_to_pack = data_dir / "canterburycorpus"

    default_compression = XarZlibCompressionSettings()
    with XarArchive(default_compression) as archive:
        archive.create_entry("docs/alice.txt", str(text_file_path), False, default_compression)

        store_compression = XarStoreCompressionSettings()
        archive.create_entry("docs/reference.html", str(html_file_path), False, store_compression)
        archive.create_entries(str(directory_to_pack), False, default_compression)

        archive.save(str(xar_output))

    print("XAR archive composed successfully.")


if __name__ == "__main__":
    run()
