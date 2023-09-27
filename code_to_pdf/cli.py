"""
Command-line interface.
"""

import click

from code_to_pdf.build import build


@click.command()
@click.argument('source_file')
@click.argument('output_file')
@click.option('--style', '-s', help="Pygments style (see https://pygments.org/styles/)")
def main(
    source_file: str,
    output_file: str,
    *,
    style: str = 'default',
) -> None:
    """
    Writes source code into a PDF document.
    """

    with open(source_file, 'r', encoding='utf-8') as file_:
        source_code = file_.read()

    pdf_content = build(
        source_code,
        source_file,
        style=style,
    )

    with open(output_file, 'wb') as file_:
        file_.write(pdf_content)
