Code-to-PDF
===========

.. image::
    https://img.shields.io/badge/v1.2.0-_?label=documentation
    :target: https://victorbnl.github.io/code-to-pdf/

Generate PDF documents from source code with syntax highlighting.

.. image::
    https://github.com/victorbnl/code-to-pdf/blob/main/docs/_static/artwork.png?raw=true

Motivation
----------

I created this project because my school teacher preferred to get our homework
as PDF files rather than source files. So I figured I’d automate it to save
myself from copying the code in LibreOffice Writer for each homework.

Requirements
------------

- pdflatex

Installation
------------

.. code-block::

    pip install git+https://github.com/victorbnl/code-to-pdf

Usage
-----

As a command-line application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

    usage: code-to-pdf [-h] [-s STYLE] [--font-size FONT_SIZE] [--linenos LINENOS] [--linenostep LINENOSTEP] [--page-numbers PAGE_NUMBERS]
                       [--paper-size PAPER_SIZE] [--top-margin TOP_MARGIN] [--bottom-margin BOTTOM_MARGIN] [--left-margin LEFT_MARGIN]
                       [--right-margin RIGHT_MARGIN]
                       source_file out_file

    positional arguments:
      source_file           file to get source code from
      out_file              output PDF file

    options:
      -h, --help            show this help message and exit
      -s STYLE, --style STYLE
                            pygments style (see https://pygments.org/styles/)
      --font-size FONT_SIZE
                            document font size
      --linenos LINENOS     whether or not to display line numbers
      --linenostep LINENOSTEP
                            if `linenos` is enabled, print every n-th line number
      --page-numbers PAGE_NUMBERS
                            whether or not to print page numbers
      --paper-size PAPER_SIZE
                            page format of resulting document
      --top-margin TOP_MARGIN
                            document top margin
      --bottom-margin BOTTOM_MARGIN
                            document bottom margin
      --left-margin LEFT_MARGIN
                            document left margin
      --right-margin RIGHT_MARGIN
                            document right margin

.. note::
    See `Pygments styles`_ for a list of available styles.

As a module
^^^^^^^^^^^

.. code-block::

    >>> import code_to_pdf
    >>> source = "print('Hello world!')"
    >>> options = code_to_pdf.Options()
    >>> pdf_content = code_to_pdf.build(source, options=options)
    >>> with open('output.pdf', 'wb') as output_file:
    ...     output_file.write(pdf_content)

.. note::
    See `Options`_ for a list of options.

Thanks to
---------

- `Pygments`_, which this project highly relies upon.

.. _Pygments styles: https://pygments.org/styles/
.. _Options: https://victorbnl.github.io/code-to-pdf/options.html
.. _Pygments: https://pygments.org/
