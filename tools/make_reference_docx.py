#!/usr/bin/env python3
"""Generate templates/journal-reference.docx for pandoc --reference-doc.

Strategy: pandoc's own default reference.docx already defines every style that
pandoc emits, so we start from it (via `pandoc --print-default-data-file
reference.docx`), then override page setup and the handful of styles whose
formatting we care about using python-docx (falling back to raw XML for the
font names, which live on w:rFonts).
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import zipfile

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "templates", "journal-reference.docx")

FONT = "Times New Roman"
MM = 1440  # unused placeholder kept for clarity


def get_default_reference(path: str) -> None:
    """Write pandoc's default reference.docx to `path`."""
    with open(path, "wb") as fh:
        subprocess.run(
            ["pandoc", "--print-default-data-file", "reference.docx"],
            stdout=fh,
            check=True,
        )


def set_run_font(run, name: str, size: float, bold: bool | None = None,
                 italic: bool | None = None) -> None:
    """Set font name on ascii/hAnsi/cs via raw XML plus size/bold/italic."""
    run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(
        "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts"
    )
    if rFonts is None:
        from docx.oxml.ns import qn
        from docx.oxml import OxmlElement

        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rFonts.set(
            "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
            + attr.split(":")[1],
            name,
        )


def set_style_font_xml(style, name: str) -> None:
    """Set w:rFonts ascii/hAnsi/cs on a style's rPr."""
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:cs"), name)


def main() -> int:
    tmp = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
    tmp.close()
    try:
        get_default_reference(tmp.name)
        doc = Document(tmp.name)
    finally:
        if os.path.exists(tmp.name):
            os.unlink(tmp.name)

    # --- page setup: A4, 2.5 cm margins on every side ---------------------
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    # --- styles -----------------------------------------------------------
    styles = doc.styles

    normal = styles["Normal"]
    set_style_font_xml(normal, FONT)
    normal.font.size = Pt(11)
    normal.font.name = FONT
    pf = normal.paragraph_format
    pf.line_spacing = 1.15
    pf.space_after = Pt(6)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    def style(name):
        try:
            return styles[name]
        except KeyError:
            return None

    title = style("Title")
    if title is not None:
        set_style_font_xml(title, FONT)
        title.font.size = Pt(14)
        title.font.bold = True
        title.font.name = FONT
        title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    author = style("Author")
    if author is not None:
        set_style_font_xml(author, FONT)
        author.font.size = Pt(11)
        author.font.name = FONT
        author.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    abstract = style("Abstract")
    if abstract is not None:
        set_style_font_xml(abstract, FONT)
        abstract.font.size = Pt(10)
        abstract.font.italic = False
        abstract.font.name = FONT
        apf = abstract.paragraph_format
        apf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        apf.line_spacing = 1.0

    h1 = style("Heading 1")
    if h1 is not None:
        set_style_font_xml(h1, FONT)
        h1.font.size = Pt(11)
        h1.font.bold = True
        h1.font.italic = False
        h1.font.name = FONT
        h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    h2 = style("Heading 2")
    if h2 is not None:
        set_style_font_xml(h2, FONT)
        h2.font.size = Pt(11)
        h2.font.bold = True
        h2.font.italic = False
        h2.font.name = FONT
        h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # --- Sinta front matter / abstract paragraph styles -------------------
    def ensure_style(name, size, alignment, bold=False):
        st = style(name)
        if st is None:
            st = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        set_style_font_xml(st, FONT)
        st.font.size = Pt(size)
        st.font.bold = bold
        st.font.italic = False
        st.font.name = FONT
        st.paragraph_format.alignment = alignment
        return st

    ensure_style("AbstractTitle", 11, WD_ALIGN_PARAGRAPH.CENTER, bold=True)
    ensure_style("SintaMasthead", 9, WD_ALIGN_PARAGRAPH.CENTER)
    ensure_style("SintaAffiliation", 10, WD_ALIGN_PARAGRAPH.CENTER)
    ensure_style("SintaKeywords", 10, WD_ALIGN_PARAGRAPH.JUSTIFY)

    for name in ("BodyText", "Body Text", "FirstParagraph", "First Paragraph"):
        st = style(name)
        if st is not None:
            st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    compact = style("Compact")
    if compact is not None:
        set_style_font_xml(compact, FONT)
        compact.font.size = Pt(10)
        compact.font.name = FONT

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
