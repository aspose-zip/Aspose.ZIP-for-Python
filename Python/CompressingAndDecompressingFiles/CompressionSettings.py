from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import (
    ArchiveEntrySettings,
    Bzip2CompressionSettings,
    LzmaCompressionSettings,
    PPMdCompressionSettings,
    EnhancedDeflateCompressionSettings,
    StoreCompressionSettings,
    XzCompressionSettings,
    ZstandardCompressionSettings,
)


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    using_bzip2_compression_settings(data_dir, output_dir)
    using_lzma_compression_settings(data_dir, output_dir)
    using_ppmd_compression_settings(data_dir, output_dir)
    using_enhanced_deflate_compression_settings(data_dir, output_dir)
    using_store_compression_settings(data_dir, output_dir)
    using_xz_compression_settings(data_dir, output_dir)
    using_zstandard_compression_settings(data_dir, output_dir)


def using_bzip2_compression_settings(data_dir, output_dir):
    with open(output_dir / "Bzip2Compression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(Bzip2CompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


def using_lzma_compression_settings(data_dir, output_dir):
    with open(output_dir / "LZMACompression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(LzmaCompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


def using_ppmd_compression_settings(data_dir, output_dir):
    with open(output_dir / "PPMdCompression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(PPMdCompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


def using_enhanced_deflate_compression_settings(data_dir, output_dir):
    with open(output_dir / "EnhancedDeflateCompression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(EnhancedDeflateCompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


def using_store_compression_settings(data_dir, output_dir):
    with open(output_dir / "StoreCompression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(StoreCompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


def using_xz_compression_settings(data_dir, output_dir):
    with open(output_dir / "XzCompression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(XzCompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


def using_zstandard_compression_settings(data_dir, output_dir):
    with open(output_dir / "ZstandardCompression_out.zip", "wb") as zip_file:
        with Archive(ArchiveEntrySettings(ZstandardCompressionSettings())) as archive:
            archive.create_entry("sample.txt", str(data_dir / "sample.txt"))
            archive.save(zip_file)


if __name__ == "__main__":
    run()
