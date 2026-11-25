from pathlib import Path

from aspose.zip import Archive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "different_password.zip", "rb") as zip_file:
        with Archive(zip_file) as archive:
            archive.entries[0].extract(str(output_dir / "alice29_extracted_pass_out.txt"), "first_pass")
            archive.entries[1].extract(str(output_dir / "asyoulik_extracted_pass_out.txt"), "second_pass")


if __name__ == "__main__":
    run()
