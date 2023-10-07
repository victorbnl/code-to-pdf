# Code to PDF

> Generate PDF documents from source code with syntax highlighting.

<p align="center">
    <img src=".readme/screenshot.png">
</p>

## Motivation

I created this project because my school teacher preferred to get our homework as PDF files rather than source files. So I figured I’d automate it to save myself from copying the code in LibreOffice Writer for each homework.

## Requirements

- `pdflatex`

## Installation

```
pip install git+https://github.com/victorbnl/code-to-pdf
```

## Usage

```
Usage: code-to-pdf [OPTIONS] SOURCE_FILE OUTPUT_FILE

  Generate PDF documents from source code with syntax highlighting.

Options:
  -s, --style TEXT      pygments style (see https://pygments.org/styles/)
  --font-size TEXT      document font size
  --top-margin TEXT     document top margin
  --bottom-margin TEXT  document bottom margin
  --left-margin TEXT    document left margin
  --right-margin TEXT   document right margin
  --help                Show this message and exit.
```

**Note:** See [Pygments’ documentation](https://pygments.org/styles/) for a list of available styles.

## Thanks to

- [Pygments](https://pygments.org/), which this project highly relies upon
