"""Command-line interface for code-to-pdf."""

from dataclasses import fields

from code_to_pdf.cli.args import parse_args
from code_to_pdf.options import StyleOptions
from code_to_pdf.build import build


def main() -> None:
    """Main function."""

    args = parse_args()

    source_file = args.source_file
    out_file = args.out_file

    style_args = {}
    field_names = [field.name for field in fields(StyleOptions)]
    for name, value in vars(args).items():
        if name in field_names:
            style_args[name] = value
    style_options = StyleOptions(**style_args)

    with open(source_file, 'r', encoding='utf-8') as file_:
        source_code = file_.read()

    pdf_content = build(source_code, source_file, style_options=style_options)

    with open(out_file, 'wb') as file_:
        file_.write(pdf_content)
