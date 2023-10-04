"""Build a document with source code."""

from code_to_pdf.build.latex import LatexBuilder
from code_to_pdf.build.pdf import PdfBuilder
from code_to_pdf.options import StyleOptions


def build(
    source_code: str,
    filename: str | None = None,
    *,
    style_options: StyleOptions,
) -> bytes:
    """Return PDF file content from source code."""

    latex_builder = LatexBuilder(style_options)
    latex_code = latex_builder.build(source_code, filename)

    pdf_builder = PdfBuilder()
    pdf_content = pdf_builder.build(latex_code)

    return pdf_content
