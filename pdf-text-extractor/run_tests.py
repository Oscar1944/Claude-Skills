#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test runner for pdf-text-extractor skill
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import io

# Set UTF-8 encoding for output
if sys.platform == "win32":
    import codecs
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from extract_and_analyze import (
    read_and_extract,
    analyze_and_answer,
    generate_summary_pdf,
)

def get_pdf_path():
    """Get PDF file path from command line argument or user input."""
    # Check for command line argument
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        print(f"Using PDF file from argument: {pdf_path}\n")
    else:
        # Prompt user for input
        print("=" * 80)
        print("PDF Text Extractor - Test Suite")
        print("=" * 80)
        print("\n[INPUT] Please provide the path to a PDF file:")
        pdf_path = input("PDF file path: ").strip()
        print()

    # Validate file exists
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        print(f"[ERROR] File not found: {pdf_path}")
        return None

    # Validate file is a PDF
    if pdf_file.suffix.lower() != ".pdf":
        print(f"[ERROR] Invalid file format. Expected .pdf, got {pdf_file.suffix}")
        return None

    return str(pdf_file.absolute())


def run_tests():
    """Run all test cases for pdf-text-extractor"""

    # API key should be set via environment variable
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("[ERROR] ANTHROPIC_API_KEY environment variable not set")
        print("Please set: $env:ANTHROPIC_API_KEY = 'your-api-key'")
        print("\nExample:")
        print("  PowerShell: $env:ANTHROPIC_API_KEY = 'your-api-key-here'")
        print("  Bash:       export ANTHROPIC_API_KEY='your-api-key-here'")
        return False

    # Get PDF file path from user
    pdf_path = get_pdf_path()
    if pdf_path is None:
        return False

    print("=" * 80)
    print("PDF Text Extractor - Test Suite")
    print("=" * 80)
    print()

    results = {
        "timestamp": datetime.now().isoformat(),
        "tests": []
    }

    # Test 1: Read and Extract
    print("[TEST 1] Read and Extract PDF")
    print("-" * 80)
    try:
        result = read_and_extract(pdf_path)
        print(f"[OK] Status: {result.get('status')}")
        print(f"[OK] Filename: {result.get('filename')}")
        print(f"[OK] Pages: {result.get('pages')}")
        print(f"[OK] Text Length: {result.get('text_length')} characters")
        print(f"[OK] Content Preview: {result.get('content_preview')[:100]}...")

        results["tests"].append({
            "id": 1,
            "name": "Read and Extract",
            "status": "passed" if result.get("status") == "success" else "failed",
            "result": result
        })
        print("[PASS] TEST 1 PASSED\n")
    except Exception as e:
        print(f"[FAIL] TEST 1 FAILED: {e}\n")
        results["tests"].append({
            "id": 1,
            "name": "Read and Extract",
            "status": "failed",
            "error": str(e)
        })

    # Test 2: Answer Question
    print("[TEST 2] Answer Question About PDF")
    print("-" * 80)
    question = "Based on the PDF, explain the differences between sparse MoE and dense MoE architectures."
    try:
        print(f"Question: {question}\n")
        answer = analyze_and_answer(pdf_path, question)

        # Handle encoding issues with special characters
        try:
            print(f"Answer:\n{answer[:500]}\n")
        except UnicodeEncodeError:
            # If there are encoding issues, save to file instead
            answer_file = Path(__file__).parent / "test_output" / "answer_output.txt"
            answer_file.parent.mkdir(parents=True, exist_ok=True)
            with open(answer_file, 'w', encoding='utf-8') as f:
                f.write(answer)
            print(f"[Note] Answer saved to file due to encoding: {answer_file}\n")

        results["tests"].append({
            "id": 2,
            "name": "Answer Question",
            "status": "passed",
            "question": question,
            "answer_preview": answer[:200] + "..." if len(answer) > 200 else answer
        })
        print("[PASS] TEST 2 PASSED\n")
    except Exception as e:
        print(f"[FAIL] TEST 2 FAILED: {e}\n")
        results["tests"].append({
            "id": 2,
            "name": "Answer Question",
            "status": "failed",
            "error": str(e)
        })

    # Test 3: Generate Summary PDF
    print("[TEST 3] Generate Summary PDF")
    print("-" * 80)
    try:
        output_path = str(Path(__file__).parent / "test_output")
        result = generate_summary_pdf(pdf_path, output_path)
        print(f"[OK] {result}\n")

        # Check if file was actually created
        pdf_files = list(Path(output_path).glob("*.pdf"))
        if pdf_files:
            pdf_file = pdf_files[0]
            file_size = pdf_file.stat().st_size
            print(f"[OK] Generated file: {pdf_file.name}")
            print(f"[OK] File size: {file_size} bytes")

            results["tests"].append({
                "id": 3,
                "name": "Generate Summary PDF",
                "status": "passed",
                "output_file": str(pdf_file),
                "file_size": file_size
            })
            print("[PASS] TEST 3 PASSED\n")
        else:
            print("[FAIL] TEST 3 FAILED: No PDF file generated\n")
            results["tests"].append({
                "id": 3,
                "name": "Generate Summary PDF",
                "status": "failed",
                "error": "No PDF file generated"
            })
    except Exception as e:
        print(f"[FAIL] TEST 3 FAILED: {e}\n")
        results["tests"].append({
            "id": 3,
            "name": "Generate Summary PDF",
            "status": "failed",
            "error": str(e)
        })

    # Summary
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    passed = sum(1 for t in results["tests"] if t["status"] == "passed")
    total = len(results["tests"])
    print(f"Passed: {passed}/{total}")
    print()

    # Save results
    results_file = Path(__file__).parent / "test_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"[OK] Results saved to: {results_file}")

    return passed == total

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
