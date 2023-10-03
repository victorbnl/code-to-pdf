"""Command-line interface for code-to-pdf."""

import click

from code_to_pdf.build import build


@click.command()
@click.argument('source_file')
@click.argument('output_file')
@click.option(
    '--style',
    '-s',
    default='default',
    help="pygments style (see https://pygments.org/styles/)"
)
@click.option(
    '--font-size',
    default='10pt',
    help="document font size"
)
def main(
    source_file: str,
    output_file: str,
    *,
    style: str,
    font_size: str,
) -> None:
    """Generate PDF documents from source code with syntax highlighting."""

    with open(source_file, 'r', encoding='utf-8') as file_:
        source_code = file_.read()

    pdf_content = build(
        source_code,
        source_file,
        style=style,
        font_size=font_size,
    )

    with open(output_file, 'wb') as file_:
        file_.write(pdf_content)
