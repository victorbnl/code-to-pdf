"""
Builds PDF content from LaTeX code.
"""

from os import path
import tempfile
import subprocess


class PdfBuilder:
    """
    Builds PDF content from LaTeX code.
    """

    def __init__(self, *, pdflatex: str = 'pdflatex'):

        self.pdflatex = pdflatex

    def build(self, latex_code: str):

        with tempfile.TemporaryDirectory() as tmpdir:

            with open(
                path.join(tmpdir, 'output.tex'), 'w', encoding='utf-8'
            ) as tex_file:
                tex_file.write(latex_code)

            try:
                subprocess.run(
                    [self.pdflatex, '-halt-on-error', 'output.tex'],
                    cwd=tmpdir,
                    check=True,
                    capture_output=True,
                )
            except subprocess.CalledProcessError as error:
                print(error.stdout.decode('utf-8'))
                raise error

            with open(path.join(tmpdir, 'output.pdf'), 'rb') as pdf_file:
                pdf_content = pdf_file.read()

            return pdf_content
