from pathlib import Path

from aspose.zip.saving import (
    SevenZipBZip2CompressionSettings,
    SevenZipEntrySettings,
    SevenZipLZMA2CompressionSettings,
    SevenZipLZMACompressionSettings,
    SevenZipPPMdCompressionSettings,
    SevenZipStoreCompressionSettings,
)
from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)


    for compression, filename in (
        (SevenZipLZMA2CompressionSettings, "SevenZip_lzma2.7z"),
        (SevenZipLZMACompressionSettings, "SevenZip_lzma.7z"),
        (SevenZipBZip2CompressionSettings, "SevenZip_bzip2.7z"),
        (SevenZipPPMdCompressionSettings, "SevenZip_ppmd.7z"),
        (SevenZipStoreCompressionSettings, "SevenZip_store.7z"),
    ):
        with SevenZipArchive(SevenZipEntrySettings(compression())) as archive:
            archive.create_entries(str(data_dir))
            archive.save(str(output_dir / filename))

    print("Successfully Created a Seven Zip Files")


if __name__ == "__main__":
    run()
