from pathlib import Path

from aspose.zip.wim import WimArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "corpus.wim", "rb") as source:
        with WimArchive(source) as archive:
            archive.images[0].extract_to_directory(str(output_dir / "DecompressWim_out"))


if __name__ == "__main__":
    run()
