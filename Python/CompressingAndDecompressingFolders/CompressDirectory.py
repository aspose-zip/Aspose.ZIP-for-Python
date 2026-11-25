from pathlib import Path

from aspose.zip import Archive


def run(output_dir: Path):
    root = Path(__file__).resolve().parents[2]
    data_dir = root / "Data"
    output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "CompressDirectory_out.zip", "wb") as zip_file:
        with open(output_dir / "CompressDirectory2_out.zip", "wb") as zip_file2:
            with Archive() as archive:
                corpus = data_dir / "canterburycorpus"

                archive.create_entries(corpus)
                archive.save(zip_file)
                archive.save(zip_file2)


if __name__ == "__main__":
    example = Path(__file__).resolve()
    run(Path("Output") / example.parent.name / example.stem)
