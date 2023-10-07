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
    """Return PDF file content from source code."""

    latex_builder = LatexBuilder(options)
    latex_code = latex_builder.build(source_code, filename)

    pdf_builder = PdfBuilder()
    pdf_content = pdf_builder.build(latex_code)

    return pdf_content
