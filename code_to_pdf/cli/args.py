"""Parse command-line arguments."""

from argparse import ArgumentParser, Namespace

import docstring_parser

from code_to_pdf.options import Options, short_aliases


def format_help(help_text: str) -> str:
    """Format `help_text` for command-line interface help."""

    if len(help_text) != 0:
        if len(help_text) == 1:
            help_text = help_text.lower()
        else:
            help_text = help_text[0].lower() + help_text[1:]

        help_text = help_text.rstrip(".")

    return help_text


def parse_args() -> Namespace:
    """Parse arguments."""

    if Options.__doc__:
        params = {
            param.arg_name: param.description or ""
            for param in docstring_parser.parse(Options.__doc__).params
        }
    else:
        params = {}

    argparser = ArgumentParser()
    argparser.add_argument("source_file", help="file to get source code from")
    argparser.add_argument("out_file", help="output PDF file")
    for name, default in Options().model_dump().items():
        flags = [f'--{name.replace("_", "-")}']
        if name in short_aliases:
            flags.insert(0, f"-{short_aliases[name]}")
        argparser.add_argument(
            *flags, default=default, help=format_help(params.get(name, ""))
        )

    return argparser.parse_args()
