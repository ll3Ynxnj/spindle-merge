# Spindle

Spindle is a command-line tool to merge files with support for wildcard paths.

## Features

- Merge multiple files into a single output file.
- Supports wildcard patterns (e.g., `*.txt`) for flexible file selection.
- **Automatically reads the list of files from `SpindleLists.txt` in the current directory.**
- Easy-to-use command-line interface.

## Installation

### From PyPI

After publishing to PyPI, you can install Spindle using `pip`:

```bash
pip install spindle
```

### From Source

Clone the repository and install using `pip`:

```bash
git clone https://github.com/ll3ynxnj/spindle.git
cd spindle
pip install .
```

## Usage

After installation, use the `spindle` command in your terminal.

### Basic Usage

Simply run:

```bash
spindle -o <output_file>
```

- The tool always reads `SpindleLists.txt` from the current directory.
- `-o <output_file>`: (Optional) Path to the output file. Defaults to `merged_output.txt` if not specified.

### Example

1. **Create a file list (`SpindleLists.txt`)**:

    ```txt
    # List of files to merge
    ~/projects/example/file1.txt
    ~/projects/example/*.log
    ~/projects/example/subdir/*.txt
    ```

2. **Run Spindle**:

    ```bash
    spindle -o combined_output.txt
    ```

    This command merges all specified files into `combined_output.txt`.

### Help

For more options and usage information, use the `--help` flag:

```bash
spindle --help
```

Example output:

```
usage: spindle [-h] [-o OUTPUT]

Spindle: Merges files listed in SpindleLists.txt.

optional arguments:
  -h, --help           show this help message and exit
  -o OUTPUT, --output OUTPUT
                       Output file path (default: merged_output.txt)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/ll3ynxnj/spindle).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
