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
@click.option(
    '--top-margin',
    default='0.4in',
    help="document top margin"
)
@click.option(
    '--bottom-margin',
    default='0.4in',
    help="document bottom margin"
)
@click.option(
    '--left-margin',
    default='0.5in',
    help="document left margin"
)
@click.option(
    '--right-margin',
    default='0.5in',
    help="document right margin"
)
def main(
    source_file: str,
    output_file: str,
    *,
    style: str,
    font_size: str,
    top_margin: str,
    bottom_margin: str,
    left_margin: str,
    right_margin: str,
) -> None:
    """Generate PDF documents from source code with syntax highlighting."""

    with open(source_file, 'r', encoding='utf-8') as file_:
        source_code = file_.read()

    pdf_content = build(
        source_code,
        source_file,
        style=style,
        font_size=font_size,
        top_margin=top_margin,
        bottom_margin=bottom_margin,
        left_margin=left_margin,
        right_margin=right_margin,
    )

    with open(output_file, 'wb') as file_:
        file_.write(pdf_content)
