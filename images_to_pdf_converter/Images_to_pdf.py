import os
import sys
import argparse
import img2pdf

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')


def images_to_pdf(image_folder_path, output_path=None):
    """Convert all images in a folder to a single PDF file.

    Args:
        image_folder_path (str): Path to the folder containing images.
        output_path (str, optional): Path for the output PDF file.
                                     Defaults to 'Output.pdf' inside the image folder.
    """
    # Validate the folder path
    if not os.path.exists(image_folder_path):
        print(f"Error: Folder not found — '{image_folder_path}'")
        sys.exit(1)

    if not os.path.isdir(image_folder_path):
        print(f"Error: '{image_folder_path}' is not a directory.")
        sys.exit(1)

    # Collect and sort supported images
    images = sorted(
        f for f in os.listdir(image_folder_path)
        if f.lower().endswith(SUPPORTED_EXTENSIONS)
    )

    if not images:
        print(f"No supported images ({', '.join(SUPPORTED_EXTENSIONS)}) found in '{image_folder_path}'.")
        sys.exit(1)

    print(f"Found {len(images)} image(s). Converting to PDF...")

    # Default output path: inside the image folder
    if output_path is None:
        output_path = os.path.join(image_folder_path, "Output.pdf")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read image bytes
    images_bytes = []
    for filename in images:
        filepath = os.path.join(image_folder_path, filename)
        with open(filepath, "rb") as img_file:
            images_bytes.append(img_file.read())

    # Convert and write PDF
    pdf_bytes = img2pdf.convert(images_bytes)
    with open(output_path, "wb") as pdf_file:
        pdf_file.write(pdf_bytes)

    print(f"PDF saved to: {os.path.abspath(output_path)}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert a folder of images into a single PDF."
    )
    parser.add_argument(
        "folder",
        help="Path to the folder containing images."
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Path for the output PDF file (default: Output.pdf inside the image folder)."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    images_to_pdf(args.folder, args.output)
