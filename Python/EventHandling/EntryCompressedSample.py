from pathlib import Path

from aspose.zip import Archive
from aspose.zip.saving import ArchiveSaveOptions, EventsBag


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    source_path = data_dir / "lcet10.txt"

    save_options = ArchiveSaveOptions()
    save_options.events_bag = EventsBag()

    def on_entry_compressed(sender, args):
        print(f"Entry '{args.entry.name}' compressed.")

    if hasattr(save_options.events_bag, "entry_compressed"):
        save_options.events_bag.entry_compressed += on_entry_compressed

    with Archive() as archive:
        with open(source_path, "rb") as source1:
            archive.create_entry("lcet10.txt", source1)

            second_path = data_dir / "alice29.txt"
            with open(second_path, "rb") as source2:
                archive.create_entry("alice29.txt", source2)

                out_path = output_dir / "entry_compressed_sample.zip"
                archive.save(str(out_path), save_options)


if __name__ == "__main__":
    run()
