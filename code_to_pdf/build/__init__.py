"""Build a document with source code."""

from code_to_pdf.build.latex import LatexBuilder
from code_to_pdf.build.pdf import PdfBuilder
from code_to_pdf.options import Options


def build(
    source_code: str,
    filename: str | None = None,
    *,
    options: Options,
) -> bytes:
    """
    Build PDF with `source_code`.

    Args:
        source_code: Code to build the PDF from.
        filename: Source file name (used for Pygments lexer lookup, optional).
        options: Document generation options.

    Return:
        Byte array with the contents of the generated PDF file.
    """

    latex_builder = LatexBuilder(options)
    latex_code = latex_builder.build(source_code, filename)

    pdf_builder = PdfBuilder()
    pdf_content = pdf_builder.build(latex_code)

    return pdf_content
