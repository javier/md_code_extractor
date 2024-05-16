
# Extract Code Blocks from Markdown/Docusaurus Project

This Python script extracts all code blocks from a Markdown or Docusaurus project and outputs them to a specified markdown file. The code blocks are sorted by file paths in alphabetical order for easier navigation.

## Features

- Extracts fenced code blocks (`` ``` ``).
- Outputs extracted code blocks to a specified markdown file.
- Sorts files and folders alphabetically for easy navigation.

## Requirements

- Python 3.6 or higher

## Usage

1. Clone the repository to your local machine.
    ```sh
    git clone https://github.com/javier/md_code_extractor.git
    cd md_code_extractor
    ```

2. Run the script, providing the path to the Docusaurus repository and the desired output markdown file name as arguments:
    ```sh
    python md_code_extractor.py <project_path> <output_file.md>
    ```

    Replace `<project_path>` with the path to the project and `<output_file.md>` with the desired name of the output markdown file.

## Example

```sh
python md_code_extractor.py /path/to/your/docs extracted_code_blocks.md
```

This command will create a `extracted_code_blocks.md` file containing all code blocks from the specified project.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
