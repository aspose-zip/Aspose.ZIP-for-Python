from io import BytesIO
from pathlib import Path
from shutil import copyfileobj

from aspose.zip import Archive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with Archive(str(data_dir / "outer.zip")) as outer:
        entries_to_delete = []
        entries_to_insert = []

        for entry in outer.entries:
            if entry.name.lower().endswith(".zip"):
                entries_to_delete.append(entry)

                with BytesIO() as inner_compressed:
                    with entry.open() as source:
                        copyfileobj(source, inner_compressed)

                    with Archive(inner_compressed) as inner:
                        for inner_entry in inner.entries:
                            content = BytesIO()

                            with inner_entry.open() as source:
                                copyfileobj(source, content)

                            entries_to_insert.append((inner_entry.name, content))

        for entry in entries_to_delete:
            outer.delete_entry(entry)

        for name, content in entries_to_insert:
            outer.create_entry(name, content)

        outer.save(str(output_dir / "flatten.zip"))


if __name__ == "__main__":
    run()
