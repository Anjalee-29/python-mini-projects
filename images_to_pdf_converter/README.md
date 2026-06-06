# Images to PDF Converter

A simple Python utility to convert a folder of images into a single PDF file.

## Features

- Converts `.jpg`, `.jpeg`, `.png`, and `.gif` images into a single PDF
- Automatically sorts images alphabetically before merging
- Accepts arguments via the command line — no need to edit the script
- Saves the output PDF inside the image folder by default, or to a custom path

## Requirements

- Python 3.x
- [img2pdf](https://pypi.org/project/img2pdf/)

Install the dependency with:

```bash
pip install img2pdf
```

## Usage

```bash
python images_to_pdf.py <folder> [-o <output_path>]
```

### Arguments

| Argument | Description |
|---|---|
| `folder` | Path to the folder containing images (**required**) |
| `-o`, `--output` | Path for the output PDF file (optional) |

### Examples

**Basic usage** — output saved as `Output.pdf` inside the image folder:

```bash
python images_to_pdf.py /path/to/images
```

**Custom output path:**

```bash
python images_to_pdf.py /path/to/images -o /path/to/result.pdf
```

## Example

If your folder contains:

```
images/
├── page1.jpg
├── page2.jpg
└── page3.png
```

Running:

```bash
python images_to_pdf.py images/
```

Produces `images/Output.pdf` with all three images merged in alphabetical order.

## Notes

- Images are sorted alphabetically, so naming them numerically (e.g., `001.jpg`, `002.jpg`) ensures the correct page order.
- Case-insensitive extension matching — `.JPG` and `.jpg` are both supported.
- The script exits with a clear error message if the folder doesn't exist or contains no supported images.
