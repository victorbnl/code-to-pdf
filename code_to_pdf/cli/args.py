"""Parse command-line arguments."""

from dataclasses import fields
from argparse import ArgumentParser

import docstring_parser

from code_to_pdf.options import StyleOptions


def parse_args():
    """Parse arguments."""

    params = {
        param.arg_name: param.description
        for param in docstring_parser.parse(StyleOptions.__doc__).params
    }

    argparser = ArgumentParser()
    argparser.add_argument('source_file', help="file to get source code from")
    argparser.add_argument('out_file', help="output PDF file")
    for field in fields(StyleOptions):
        argparser.add_argument(
            f'--{field.name.replace("_", "-")}',
            type=field.type,
            default=field.default,
            help=params[field.name]
        )

    return argparser.parse_args()
