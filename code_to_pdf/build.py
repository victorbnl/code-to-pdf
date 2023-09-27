"""
Wrapper function around builders.
"""

from code_to_pdf.builders import LatexBuilder, PdfBuilder


def build(
    source_code: str,
    filename: str | None = None,
    style: str = 'default',
) -> bytes:
    """
    Returns the bytes of a PDF file which contains `source_code`.
    """

    latex_builder = LatexBuilder(style)
    latex_code = latex_builder.build(source_code, filename)

    pdf_builder = PdfBuilder()
    pdf_content = pdf_builder.build(latex_code)

    return pdf_content
