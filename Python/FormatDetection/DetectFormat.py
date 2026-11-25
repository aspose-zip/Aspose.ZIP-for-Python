from pathlib import Path

from aspose.zip.archiveinfo import ArchiveInstanceInfo


def run():
    data_dir = Path(__file__).resolve().parents[2] / "Data"

    for file in data_dir.glob("archive.*"):
        info = ArchiveInstanceInfo.get_archive_instance_info(str(file))
        format_info = info.format_info
        print(f"File {file.name}: detected format {format_info.format.name}")
        if hasattr(format_info, "type"):
            print(f"class {format_info.type}")


if __name__ == "__main__":
    run()
