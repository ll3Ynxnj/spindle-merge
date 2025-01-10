
# Spindle

Spindle is a command-line tool to merge files with support for wildcard paths.

## Features

- Merge multiple files into a single output file.
- Supports wildcard patterns (e.g., `*.txt`) for flexible file selection.
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

```bash
spindle <file_list_path> -o <output_file>
```

- `<file_list_path>`: Path to the text file containing the list of files to merge.
- `-o <output_file>`: (Optional) Path to the output file. Defaults to `merged_output.txt` if not specified.

### Example

1. **Create a file list (`files.txt`)**:

    ```txt
    ~/projects/example/file1.txt
    ~/projects/example/*.log
    ~/projects/example/subdir/*.txt
    ```

2. **Run Spindle**:

    ```bash
    spindle files.txt -o combined_output.txt
    ```

    This command merges all specified files into `combined_output.txt`.

### Help

For more options and usage information, use the `--help` flag:

```bash
spindle --help
```

Example output:

```
usage: spindle [-h] [-o OUTPUT] file_list

Merge files specified in a file list.

positional arguments:
  file_list            Path to the file containing list of files to merge.

optional arguments:
  -h, --help           show this help message and exit
  -o OUTPUT, --output OUTPUT
                       Output file path (default: merged_output.txt)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/ll3Ynxnj/spindle).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
