# Aspose.Zip for Python via .NET examples

Native Python translations of the product examples in Aspose.ZIP-for-.NET.

## Running the examples

Install Aspose.Zip for Python via .NET in the Python environment you intend to use:

```shell
python -m pip install aspose-zip
```

Then run all examples from the repository root:

```shell
python run_examples.py
```

The runner checks that Aspose.Zip can be imported and used, executes every example
sequentially in one Python process, reports each result and exits with a nonzero
status if startup or any example fails.

### License

To run with a license, place a single `*.lic` file in the repository's `Lic/`
directory. Alternatively, set the `ASPOSE_ZIP_LICENSE` environment variable to
the license file path; this takes precedence over automatic discovery. If several
license files are present, the runner selects the first in sorted order, warns
which file was selected and ignores the others. Keep exactly one `*.lic` file in
`Lic/` for an unambiguous automatic choice.

Without a license, the runner displays a warning and continues in evaluation
mode; evaluation restrictions may affect example results. A missing explicitly
configured license or a license that cannot be applied stops the run. License
files in `Lic/` are ignored by Git.

Each example can also be run independently, for example:

```shell
python Python/CompressingAndDecompressingFiles/CompressSingleFile.py
```

`Data/` is the read-only input dataset. Examples write generated files to
`Output/<category>/<example>/`. A decompression example that creates its own
input archive passes its output directory to the compression example, so it does
not depend on any previous run. The all-examples runner clears the known generated
example output directories once before starting; unrelated directories are not
removed. Output files remain available for inspection afterwards.
