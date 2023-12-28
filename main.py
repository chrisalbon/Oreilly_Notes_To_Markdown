"""Reads data from a CSV file containing O'Reilly book annotations, and then
writes the annotations in Markdown format to an output file.
"""

import argparse
import csv

INPUT_FILE = "oreilly-annotations.csv"
OUTPUT_FILE = "oreilly-annotations.md"


def read_csv(file_name):
    """Reads a CSV file and returns a list of dictionaries."""
    annotation_list = []
    with open(file_name, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            annotation_list.append(row)
    return annotation_list


def write_markdown(annotations, output_file=OUTPUT_FILE):
    """Writes a list of annotations to a Markdown file."""
    with open(output_file, "w", encoding="utf-8") as md_file:
        for annotation in annotations:
            note = annotation["Personal Note"].strip()
            highlight = annotation["Highlight"].strip()
            book_title = annotation["Book Title"].strip()
            chapter_title = annotation["Chapter Title"].strip()
            book_link = annotation["Book URL"].strip()
            md_file.write(f"## {note}\n")
            md_file.write("\n")
            md_file.write(
                f'> "{highlight}" ([{book_title}, {chapter_title}]({book_link}))\n\n'
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--csv_file", default=INPUT_FILE, help="CSV file")
    args = parser.parse_args()

    annotations_file = read_csv(args.csv_file)
    write_markdown(annotations_file)
