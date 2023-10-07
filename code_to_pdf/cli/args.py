"""Parse command-line arguments."""

from argparse import ArgumentParser

import docstring_parser

from code_to_pdf.options import StyleOptions, short_aliases


def parse_args():
    """Parse arguments."""

    params = {
        param.arg_name: param.description
        for param in docstring_parser.parse(StyleOptions.__doc__).params
    }

    argparser = ArgumentParser()
    argparser.add_argument("source_file", help="file to get source code from")
    argparser.add_argument("out_file", help="output PDF file")
    for name, field in StyleOptions.__fields__.items():
        flags = [f'--{name.replace("_", "-")}']
        if name in short_aliases:
            flags.insert(0, f"-{short_aliases[name]}")
        argparser.add_argument(*flags, default=field.default, help=params[name])

    return argparser.parse_args()
