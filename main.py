# Reads data from a CSV file containing O'Reilly book annotations, and then
# writes the annotations in Markdown format to an output file.

import csv
import requests
from bs4 import BeautifulSoup


def read_csv(file_name):
    annotations = []
    with open(file_name, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            annotations.append(row)
    return annotations


def write_markdown(annotations, output_file="oreilly-annotations.md"):
    with open(output_file, "w", encoding="utf-8") as md_file:
        for annotation in annotations:
            note = annotation["Personal Note"]
            highlight = annotation["Highlight"]
            book_title = annotation["Book Title"]
            chapter_title = annotation["Chapter Title"]
            year = annotation["Year"]
            amazon = annotation["Amazon"]
            md_file.write(f"> #### {note}\n")
            md_file.write(f">\n")
            md_file.write(
                f'> "{highlight}" ([{book_title}, {chapter_title}]({amazon}), {year})\n\n'
            )


if __name__ == "__main__":
    csv_file = "oreilly-annotations.csv"
    annotations = read_csv(csv_file)
    write_markdown(annotations)
