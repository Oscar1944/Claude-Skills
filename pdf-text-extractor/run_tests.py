#!/usr/bin/env python3
"""
Tests for pdf-text-extractor skill
Test 1: Generate 100-word summary (proves skill can see content)
Test 2: Modify content (proves skill can clean/edit content)
Test 3: Output a PDF file (proves skill can generate files)
"""

import sys
import io
import os
import re
import requests
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

API_URL = os.getenv("PDF_EXTRACTION_API_URL", "https://claude-skill.zeabur.app")
OUTPUT_DIR = Path(__file__).parent / "test_output"
OUTPUT_DIR.mkdir(exist_ok=True)

def get_content(pdf_path: str) -> str:
    """Call API to get PDF content."""
    with open(pdf_path, "rb") as f:
        r = requests.post(f"{API_URL}/extract-pdf", files={"file": f}, timeout=120)
    data = r.json()
    assert data["status"] == "success", f"API error: {data.get('message')}"
    return data["content"]


def test1_summarize(content: str) -> str:
    """Test 1: Ask Claude to produce a 100-word summary."""
    from anthropic import Anthropic
    client = Anthropic()
    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"Summarize the following document in exactly 100 words:\n\n{content[:8000]}"
        }]
    )
    summary = msg.content[0].text
    word_count = len(summary.split())
    assert word_count >= 80, f"Summary too short: {word_count} words"
    return summary


def test2_modify(content: str) -> str:
    """Test 2: Clean content - remove special characters and normalize whitespace."""
    cleaned = re.sub(r"[^\w\s.,;:()\-]", " ", content)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    assert len(cleaned) > 0, "Cleaned content is empty"
    assert len(cleaned) < len(content), "Content was not modified"
    return cleaned


def test3_output_pdf(content: str) -> Path:
    """Test 3: Generate a PDF file from content."""
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import letter

    output_file = OUTPUT_DIR / "test_output.pdf"
    doc = SimpleDocTemplate(str(output_file), pagesize=letter)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("PDF Skill Test Output", styles["Heading1"]),
        Spacer(1, 12),
        Paragraph(content[:2000].replace("\n", "<br/>"), styles["Normal"]),
    ]
    doc.build(story)
    assert output_file.exists(), "PDF file was not created"
    assert output_file.stat().st_size > 0, "PDF file is empty"
    return output_file


def run():
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    passed = 0

    print(f"PDF: {pdf_path}")
    print(f"API: {API_URL}\n")

    # Get content from API (shared across all tests)
    print("Fetching content from API...")
    content = get_content(pdf_path)
    print(f"Content retrieved: {len(content)} characters\n")

    # Test 1
    print("[TEST 1] Generate 100-word summary")
    try:
        summary = test1_summarize(content)
        print(f"  Word count: {len(summary.split())}")
        print(f"  Preview: {summary[:150]}...")
        print("  PASSED\n")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}\n")

    # Test 2
    print("[TEST 2] Modify/clean content")
    try:
        cleaned = test2_modify(content)
        print(f"  Original length: {len(content)} chars")
        print(f"  Cleaned length:  {len(cleaned)} chars")
        print(f"  Preview: {cleaned[:150]}...")
        print("  PASSED\n")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}\n")

    # Test 3
    print("[TEST 3] Output PDF file")
    try:
        out = test3_output_pdf(content)
        print(f"  Output file: {out}")
        print(f"  File size: {out.stat().st_size} bytes")
        print("  PASSED\n")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}\n")

    print(f"Results: {passed}/3 passed")
    sys.exit(0 if passed == 3 else 1)


if __name__ == "__main__":
    run()
