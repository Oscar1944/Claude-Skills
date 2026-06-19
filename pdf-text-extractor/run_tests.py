#!/usr/bin/env python3
"""
Test runner for pdf-text-extractor skill
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from extract_and_analyze import (
    read_and_extract,
    analyze_and_answer,
    generate_summary_pdf,
)

def run_tests():
    """Run all test cases for pdf-text-extractor"""

    # Set API key
    os.environ["ANTHROPIC_API_KEY"] = "YOUR_API_KEY_HERE"

    pdf_path = "C:\\Users\\USER\\Desktop\\VS Code file\\claude_project\\A Survey on Mixture of Experts.pdf"

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
        print(f"Answer:\n{answer}\n")

        results["tests"].append({
            "id": 2,
            "name": "Answer Question",
            "status": "passed",
            "question": question,
            "answer": answer[:200] + "..." if len(answer) > 200 else answer
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
