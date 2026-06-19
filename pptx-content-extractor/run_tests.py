#!/usr/bin/env python3
"""
Test runner for pptx-content-extractor skill
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
    generate_summary_pptx,
)

def get_pptx_path():
    """Get PPTX file path from command line argument or user input."""
    # Check for command line argument
    if len(sys.argv) > 1:
        pptx_path = sys.argv[1]
        print(f"Using PPTX file from argument: {pptx_path}\n")
    else:
        # Prompt user for input
        print("=" * 80)
        print("PPTX Content Extractor - Test Suite")
        print("=" * 80)
        print("\n[INPUT] Please provide the path to a PPTX file:")
        pptx_path = input("PPTX file path: ").strip()
        print()

    # Validate file exists
    pptx_file = Path(pptx_path)
    if not pptx_file.exists():
        print(f"[ERROR] File not found: {pptx_path}")
        return None

    # Validate file is a PPTX
    if pptx_file.suffix.lower() != ".pptx":
        print(f"[ERROR] Invalid file format. Expected .pptx, got {pptx_file.suffix}")
        return None

    return str(pptx_file.absolute())


def run_tests():
    """Run all test cases for pptx-content-extractor"""

    # API key should be set via environment variable
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("[ERROR] ANTHROPIC_API_KEY environment variable not set")
        print("Please set: $env:ANTHROPIC_API_KEY = 'your-api-key'")
        print("\nExample:")
        print("  PowerShell: $env:ANTHROPIC_API_KEY = 'your-api-key-here'")
        print("  Bash:       export ANTHROPIC_API_KEY='your-api-key-here'")
        return False

    # Get PPTX file path from user
    pptx_path = get_pptx_path()
    if pptx_path is None:
        return False

    print("=" * 80)
    print("PPTX Content Extractor - Test Suite")
    print("=" * 80)
    print()

    results = {
        "timestamp": datetime.now().isoformat(),
        "tests": []
    }

    # Test 1: Read and Extract
    print("[TEST 1] Read and Extract PPTX")
    print("-" * 80)
    try:
        result = read_and_extract(pptx_path)
        print(f"[OK] Status: {result.get('status')}")
        print(f"[OK] Filename: {result.get('filename')}")
        print(f"[OK] Slides: {result.get('slides')}")
        print(f"[OK] Content Length: {result.get('content_length')} characters")
        print(f"[OK] First Slide Preview: {result.get('first_slide_preview')[:100]}...")

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
    print("[TEST 2] Answer Question About PPTX")
    print("-" * 80)
    question = "Based on the presentation, what are the key advantages and disadvantages of the freemium business model?"
    try:
        print(f"Question: {question}\n")
        answer = analyze_and_answer(pptx_path, question)
        print(f"Answer:\n{answer[:500]}\n")

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

    # Test 3: Generate Summary PPTX
    print("[TEST 3] Generate Summary PPTX")
    print("-" * 80)
    try:
        output_path = str(Path(__file__).parent / "test_output")
        result = generate_summary_pptx(pptx_path, output_path)
        print(f"[OK] {result}\n")

        # Check if file was actually created
        pptx_files = list(Path(output_path).glob("*.pptx"))
        if pptx_files:
            pptx_file = pptx_files[0]
            file_size = pptx_file.stat().st_size
            print(f"[OK] Generated file: {pptx_file.name}")
            print(f"[OK] File size: {file_size} bytes")

            results["tests"].append({
                "id": 3,
                "name": "Generate Summary PPTX",
                "status": "passed",
                "output_file": str(pptx_file),
                "file_size": file_size
            })
            print("[PASS] TEST 3 PASSED\n")
        else:
            print("[FAIL] TEST 3 FAILED: No PPTX file generated\n")
            results["tests"].append({
                "id": 3,
                "name": "Generate Summary PPTX",
                "status": "failed",
                "error": "No PPTX file generated"
            })
    except Exception as e:
        print(f"[FAIL] TEST 3 FAILED: {e}\n")
        results["tests"].append({
            "id": 3,
            "name": "Generate Summary PPTX",
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
