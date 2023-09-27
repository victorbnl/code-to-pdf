"""
Command-line interface.
"""

import argparse

from code_to_pdf.build import build


def main() -> None:
    """
    CLI main function.
    """

    argparser = argparse.ArgumentParser(
        description="Writes source code into a PDF document."
    )
    argparser.add_argument('source_file')
    argparser.add_argument('output_file')
    argparser.add_argument(
        '-s',
        '--style',
        default='default',
        help="Pygments style (see https://pygments.org/styles/)",
    )
    args = argparser.parse_args()

    with open(args.source_file, 'r', encoding='utf-8') as source_file:
        source_code = source_file.read()

    pdf_content = build(source_code, args.source_file, style=args.style)

    with open(args.output_file, 'wb') as output_file:
        output_file.write(pdf_content)
