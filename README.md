# Code to PDF

> Generate PDF documents from source code with syntax highlighting.

<p align="center">
    <img src=".readme/screenshot.png">
</p>

## Motivation

As a matter of fact, I created this project because my school teacher preferred to get our homework as PDF files rather than source files. So I figured I’d automate it to save myself from copying the code in LibreOffice Writer for each homework.

## Requirements

- `pdflatex`

## Installation

```
pip install git+https://github.com/victorbnl/code-to-pdf
```

## Usage

```
usage: code-to-pdf [-h] [-s STYLE] source_file output_file

Generate PDF documents from source code with syntax highlighting.

positional arguments:
  source_file
  output_file

options:
  -h, --help            show this help message and exit
  -s STYLE, --style STYLE
                        pygments style (see https://pygments.org/styles/)
```

**Note:** See [Pygments’ documentation](https://pygments.org/styles/) for a list of available styles.

## Thanks to

- [Pygments](https://pygments.org/), which this project highly relies upon
