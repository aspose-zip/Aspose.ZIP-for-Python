"""Run the Aspose.Zip Python examples sequentially in one process."""
import os
from pathlib import Path
import runpy
import shutil
import sys
from time import perf_counter
import traceback


ROOT = Path(__file__).resolve().parent
EXAMPLES = sorted((ROOT / "Python").rglob("*.py"))


def find_license(*, require_license=False):
    """Prefer the explicit license path; otherwise discover a local license."""
    license_path = os.environ.get("ASPOSE_ZIP_LICENSE")
    if require_license and not license_path:
        raise RuntimeError("ASPOSE_ZIP_LICENSE is required for CI.")
    if license_path:
        license_file = Path(license_path).resolve()
        if not license_file.is_file():
            raise FileNotFoundError(f"License file not found: {license_file}")
        return license_file

    licenses = sorted(path for path in (ROOT / "Lic").glob("*.lic")
                      if path.is_file())
    if len(licenses) > 1:
        print(
            f"WARNING: Multiple .lic files found in Lic/. "
            f"Selected {licenses[0].name!r}; all other license files are ignored.\n"
            "For an unambiguous choice, keep exactly one .lic file in Lic/.",
            file=sys.stderr, flush=True,
        )
    return licenses[0] if licenses else None


def prepare_examples(*, require_license=False):
    """Check the product, load the license and clear generated example outputs."""
    try:
        from aspose.zip import Archive, License
    except ImportError as error:
        raise RuntimeError(
            "Aspose.Zip for Python via .NET could not be imported. "
            "Install it in the current Python environment with:\n"
            "  python -m pip install aspose-zip\n"
            "If it is already installed, check its dependencies and runtime.\n"
            f"Import error: {error}"
        ) from error

    license_file = find_license(require_license=require_license)
    if license_file is None:
        print(
            "WARNING: No Aspose.Zip license found. Running in evaluation mode; "
            "evaluation restrictions may affect example results.\n"
            "To use a license, place one .lic file in the repository's Lic/ "
            "directory or set ASPOSE_ZIP_LICENSE to its path.",
            file=sys.stderr, flush=True,
        )
    else:
        try:
            License().set_license(str(license_file))
        except Exception as error:
            raise RuntimeError(
                f"Could not apply the Aspose.Zip license: {license_file}\n{error}"
            ) from error
        print(f"Aspose.Zip license loaded: {license_file.name}", flush=True)

    # Verify that the installed product can actually create an archive.
    with Archive():
        pass

    if not EXAMPLES:
        raise RuntimeError("No Python examples found.")

    for example in EXAMPLES:
        output_dir = ROOT / "Output" / example.relative_to(ROOT / "Python").with_suffix("")
        if output_dir.exists():
            shutil.rmtree(output_dir)


def run_example(example: Path):
    """Run the same entry point as a standalone invocation."""
    original_path = sys.path[:]
    sys.path.insert(0, str(example.parent))
    try:
        runpy.run_path(str(example), run_name="__main__")
    finally:
        sys.path[:] = original_path


def main():
    try:
        prepare_examples()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr, flush=True)
        return 1

    failed = []
    start = perf_counter()

    for example in EXAMPLES:
        name = example.relative_to(ROOT).as_posix()
        print(f"Running {name}", flush=True)
        example_start = perf_counter()
        try:
            run_example(example)
        except Exception:
            traceback.print_exc()
            failed.append(name)
            print(f"FAIL {name} ({perf_counter() - example_start:.2f}s)", flush=True)
        else:
            print(f"PASS {name} ({perf_counter() - example_start:.2f}s)", flush=True)

    print(f"{len(EXAMPLES) - len(failed)} passed, {len(failed)} failed in "
          f"{perf_counter() - start:.2f}s")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
