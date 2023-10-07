"""Command-line interface."""

from pydantic import ValidationError

from code_to_pdf.build import build
from code_to_pdf.cli.args import parse_args
from code_to_pdf.options import Options


def main() -> int:
    """Main function."""

    args = parse_args()

    source_file = args.source_file
    out_file = args.out_file

    style_args = {}
    for name, value in vars(args).items():
        if name in Options.__fields__:
            style_args[name] = value

    try:
        options = Options(**style_args)
    except ValidationError as exception:
        print(f"{exception.error_count()} errors in options")
        for error in exception.errors():
            print(f"{error['loc'][0]}: {error['input']}")
            if error["type"] == "assertion_error":
                print("    " + str(error["ctx"]["error"]))
            else:
                print("    " + error["msg"])
        return 1

    with open(source_file, "r", encoding="utf-8") as file_:
        source_code = file_.read()

    pdf_content = build(source_code, source_file, options=options)

    with open(out_file, "wb") as file_:
        file_.write(pdf_content)

    return 0
