#!/usr/bin/env python3
"""
PDF Text Extractor Skill
Extracts text from PDFs, answers questions about content, and generates new PDFs.
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import dependencies (will be installed via requirements.txt)
try:
    import pdfplumber
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from PIL import Image
except ImportError as e:
    logger.error(f"Missing required dependency: {e}")
    sys.exit(1)


class PDFReader:
    """Handles PDF reading and text extraction."""

    def __init__(self, file_path: str):
        """
        Initialize PDF reader.

        Args:
            file_path: Path to PDF file
        """
        self.file_path = Path(file_path)
        self.pdf = None
        self.text_content = None
        self.metadata = None

    def read_pdf(self) -> Dict:
        """Read PDF and extract basic information."""
        try:
            with pdfplumber.open(self.file_path) as pdf:
                self.pdf = pdf
                self.metadata = {
                    "filename": self.file_path.name,
                    "pages": len(pdf.pages),
                    "metadata": pdf.metadata,
                }
                self.text_content = self.extract_text()
                return {
                    "status": "success",
                    "filename": self.file_path.name,
                    "pages": len(pdf.pages),
                    "text_length": len(self.text_content),
                }
        except Exception as e:
            logger.error(f"Error reading PDF: {e}")
            return {"status": "error", "message": str(e)}

    def extract_text(self) -> str:
        """Extract all text from PDF."""
        if self.pdf is None:
            try:
                with pdfplumber.open(self.file_path) as pdf:
                    self.pdf = pdf
            except Exception as e:
                logger.error(f"Error opening PDF: {e}")
                return ""

        text_parts = []
        for page_num, page in enumerate(self.pdf.pages, 1):
            text = page.extract_text()
            if text:
                text_parts.append(f"--- Page {page_num} ---\n{text}")

        return "\n\n".join(text_parts)

    def extract_metadata(self) -> Dict:
        """Extract metadata from PDF."""
        if self.metadata is None:
            self.read_pdf()
        return self.metadata or {}

    def get_page_count(self) -> int:
        """Get total number of pages."""
        if self.metadata is None:
            self.read_pdf()
        return self.metadata.get("pages", 0) if self.metadata else 0


class DocumentAnalyzer:
    """Analyzes document content and answers questions."""

    def __init__(self, text_content: str):
        """
        Initialize analyzer with text content.

        Args:
            text_content: Extracted text from document
        """
        self.text_content = text_content
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

    def answer_question(self, question: str) -> str:
        """Answer question based on document content."""
        try:
            from anthropic import Anthropic

            client = Anthropic(api_key=self.api_key)

            system_prompt = """You are a helpful assistant that answers questions based on provided document content.
Answer based only on the information in the document. If the information is not in the document, say so clearly.
Provide detailed, well-structured answers."""

            message = client.messages.create(
                model="claude-opus-4-8",
                max_tokens=1024,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": f"Document content:\n{self.text_content}\n\nQuestion: {question}"
                    }
                ]
            )

            return message.content[0].text
        except Exception as e:
            logger.error(f"Error answering question: {e}")
            return f"Error: {str(e)}"

    def summarize(self, max_words: Optional[int] = None) -> str:
        """Generate summary of content."""
        try:
            from anthropic import Anthropic

            client = Anthropic(api_key=self.api_key)

            word_constraint = f"in approximately {max_words} words" if max_words else ""
            system_prompt = f"""You are a skilled summarizer. Create a comprehensive summary of the provided document {word_constraint}.
Include main concepts, key findings, and important conclusions. Structure the summary clearly."""

            message = client.messages.create(
                model="claude-opus-4-8",
                max_tokens=2048,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": f"Please summarize this document:\n\n{self.text_content}"
                    }
                ]
            )

            return message.content[0].text
        except Exception as e:
            logger.error(f"Error summarizing: {e}")
            return f"Error: {str(e)}"

    def extract_key_points(self, num_points: int = 5) -> List[str]:
        """Extract key points from content."""
        try:
            from anthropic import Anthropic

            client = Anthropic(api_key=self.api_key)

            message = client.messages.create(
                model="claude-opus-4-8",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": f"""Extract exactly {num_points} key points from this document.
Format each point as a single line, numbered 1-{num_points}.

Document:\n{self.text_content}"""
                    }
                ]
            )

            response_text = message.content[0].text
            points = [line.strip() for line in response_text.split('\n') if line.strip() and any(c.isdigit() for c in line[:3])]
            return points[:num_points]
        except Exception as e:
            logger.error(f"Error extracting key points: {e}")
            return []


class PDFGenerator:
    """Generates new PDF files from content."""

    def __init__(self, output_dir: str = "./output"):
        """
        Initialize PDF generator.

        Args:
            output_dir: Directory for output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_from_text(self, content: str, title: str = "Generated Document") -> str:
        """Generate PDF from text content."""
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch

            output_file = self.output_dir / f"{title.replace(' ', '_')}.pdf"

            doc = SimpleDocTemplate(
                str(output_file),
                pagesize=letter,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=18,
            )

            styles = getSampleStyleSheet()
            story = []

            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1f4788'),
                spaceAfter=30,
                alignment=1,
            )

            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 0.3 * inch))

            paragraphs = content.split('\n\n')
            for para in paragraphs:
                if para.strip():
                    story.append(Paragraph(para.strip(), styles['Normal']))
                    story.append(Spacer(1, 0.2 * inch))

            doc.build(story)
            logger.info(f"PDF generated: {output_file}")
            return str(output_file)
        except Exception as e:
            logger.error(f"Error generating PDF: {e}")
            return ""

    def generate_from_summary(self, summary: str, title: str = "Summary") -> str:
        """Generate PDF from a summary text."""
        return self.generate_from_text(summary, title)


# ============================================================================
# MAIN WORKFLOW & CLI INTERFACE
# ============================================================================

def read_and_extract(pdf_path: str) -> Dict:
    """Read PDF and extract content."""
    reader = PDFReader(pdf_path)
    result = reader.read_pdf()

    if result["status"] == "success":
        return {
            "status": "success",
            "filename": result["filename"],
            "pages": result["pages"],
            "text_length": result["text_length"],
            "content_preview": reader.text_content[:500] + "..." if len(reader.text_content) > 500 else reader.text_content,
        }
    return result


def analyze_and_answer(pdf_path: str, question: str) -> str:
    """Read PDF and answer a question about it."""
    reader = PDFReader(pdf_path)
    reader.read_pdf()

    if not reader.text_content:
        return "Error: Could not extract text from PDF"

    analyzer = DocumentAnalyzer(reader.text_content)
    return analyzer.answer_question(question)


def generate_summary_pdf(pdf_path: str, output_path: Optional[str] = None) -> str:
    """Read PDF, generate summary, and create new PDF."""
    reader = PDFReader(pdf_path)
    reader.read_pdf()

    if not reader.text_content:
        return "Error: Could not extract text from PDF"

    analyzer = DocumentAnalyzer(reader.text_content)
    summary = analyzer.summarize(max_words=500)

    generator = PDFGenerator(output_path or "./output")
    pdf_file = generator.generate_from_summary(
        summary,
        title=f"Summary of {Path(pdf_path).stem}"
    )

    if pdf_file:
        return f"Summary PDF generated: {pdf_file}"
    return "Error: Failed to generate PDF"


def main():
    """Main entry point for the skill."""
    import argparse

    parser = argparse.ArgumentParser(description="PDF Text Extractor")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    extract_parser = subparsers.add_parser("extract", help="Extract text from PDF")
    extract_parser.add_argument("pdf_path", help="Path to PDF file")

    answer_parser = subparsers.add_parser("answer", help="Answer question about PDF")
    answer_parser.add_argument("pdf_path", help="Path to PDF file")
    answer_parser.add_argument("question", help="Question to answer")

    summary_parser = subparsers.add_parser("summarize", help="Generate summary PDF")
    summary_parser.add_argument("pdf_path", help="Path to PDF file")
    summary_parser.add_argument("--output", help="Output directory")

    args = parser.parse_args()

    if args.command == "extract":
        result = read_and_extract(args.pdf_path)
        print(json.dumps(result, indent=2))
    elif args.command == "answer":
        answer = analyze_and_answer(args.pdf_path, args.question)
        print(answer)
    elif args.command == "summarize":
        result = generate_summary_pdf(args.pdf_path, args.output)
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()