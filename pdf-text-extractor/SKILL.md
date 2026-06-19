---
name: pdf-text-extractor
description: Extract text from PDF files, answer questions about PDF content, and generate new PDFs. Use this skill whenever the user needs to read a PDF, ask questions about its content, analyze a paper, extract specific information from a document, or create a new PDF based on content analysis. This is your go-to skill for any PDF manipulation task - reading, understanding, or generating documents.
license: MIT
compatibility:
  - tool: python
  - tool: file-system
---

# PDF Text Extractor

This skill enables you to:
1. **Read and extract** text content from PDF files
2. **Answer questions** about PDF content using AI analysis
3. **Generate new PDFs** from extracted content or analysis results

## When to Use This Skill

Use this skill when you need to:
- Extract and analyze content from PDF documents
- Answer specific questions about a PDF's content
- Create summarized or reformatted PDF versions
- Convert PDF content into different formats
- Analyze academic papers, reports, or documents
- Generate new PDFs based on document analysis

## Core Capabilities

### 1. PDF Reading & Text Extraction

The skill reads PDF files and extracts all text content, preserving structure where possible. It captures:
- Main text content
- Page numbers and metadata
- Document structure (chapters, sections if detectable)
- Character and word counts

**Example workflow:**
```
User: "Read this PDF and tell me what it's about"
→ Skill reads PDF
→ Extracts text and structure
→ Uses AI to generate summary/analysis
→ Returns structured information
```

### 2. Content Analysis & Question Answering

Once content is extracted, the skill uses AI language capabilities to:
- Answer specific questions based on the PDF content
- Provide summaries (full or targeted)
- Extract key information
- Analyze specific sections
- Compare information across sections

**Example workflow:**
```
User: "Based on the PDF, what are the main points about MoE architecture?"
→ Skill extracts PDF content
→ AI analyzes content in context
→ Returns detailed answer based on document
```

### 3. PDF Generation

The skill can create new PDF files:
- From analysis summaries
- From extracted sections
- With reformatted content
- With user-specified modifications

**Example workflow:**
```
User: "Generate a PDF summary of this document"
→ Skill analyzes PDF
→ Creates structured summary
→ Generates new PDF file
→ Saves and returns path to generated PDF
```

## How to Use

### Step 1: Invoke the Skill

When you mention:
- Reading a PDF
- Analyzing a document
- Asking questions about a paper
- Creating a PDF from content
- Extracting information from a document

The skill will automatically engage.

### Step 2: Provide Input

You can provide:
- File path to a PDF (e.g., `C:/path/to/document.pdf`)
- Your question or task (e.g., "Summarize this paper", "What's the main argument?")
- Preferences for output format (optional)

### Step 3: Receive Output

The skill returns:
- **For reading/analysis**: Text content, summaries, answers to your questions
- **For generation**: Path to newly generated PDF file
- **Metadata**: Document info, page count, key statistics

## Usage Examples

### Example 1: Read and Summarize
```
User: "Read A Survey on Mixture of Experts.pdf and give me a 100-word summary"

Process:
1. Reads PDF file
2. Extracts all text
3. Uses AI to generate concise summary
4. Returns summary text

Output:
"This comprehensive survey examines Mixture of Experts (MoE) architectures...
[100 words of summary]"
```

### Example 2: Answer Questions
```
User: "Based on the PDF, what is sparse MoE and how does it differ from dense MoE?"

Process:
1. Reads PDF
2. Finds relevant sections
3. Uses AI to formulate answer
4. Returns detailed explanation

Output:
"Sparse MoE activates only a subset of experts...
[detailed explanation based on PDF content]"
```

### Example 3: Generate PDF from Analysis
```
User: "Create a new PDF that contains just the key takeaways from this document"

Process:
1. Reads PDF
2. Analyzes content
3. Extracts key points
4. Generates new formatted PDF
5. Saves file

Output:
"Generated PDF: /output/key-takeaways.pdf (1.2 MB, 3 pages)"
```

## Technical Details

### Supported PDF Features
- Text extraction (standard and scanned PDFs with OCR capability)
- Metadata extraction (author, title, creation date, etc.)
- Page structure recognition
- Table detection (basic)
- Image extraction (optional)

### Output Formats
- **Text**: Plain text or Markdown
- **Data**: JSON with structured information
- **Files**: Generated PDF files with preserved formatting

### File Size Limits
- Input: PDFs up to 50 MB
- Output: Generated files up to 100 MB
- Processing time depends on PDF complexity and size

## Important Notes

### Accuracy
- The skill works best with text-based PDFs
- Scanned PDFs (image-based) may have lower accuracy
- Complex layouts may require additional processing

### Privacy
- PDFs are processed locally
- Content is used only for the specified task
- Files are not stored permanently unless you save the generated outputs

### Performance Tips
- For large PDFs, specific questions yield faster, more focused results
- Summaries of very long documents may need length specifications
- Multiple related tasks can be batched together

## Limitations

- Very large PDFs (>50 MB) may timeout
- Highly specialized formatting may not be fully preserved
- Scanned PDFs (non-text) require OCR and may have accuracy limits
- Some encrypted or DRM-protected PDFs cannot be read

## Getting Help

If the skill doesn't work as expected:
1. Verify the PDF file path is correct and readable
2. Check if the PDF is encrypted or protected
3. For large files, try breaking the task into smaller chunks
4. Provide specific questions for better results

---

## Next Steps

Once you've used this skill and received results, you can:
- Ask follow-up questions about the same PDF
- Request different analysis angles
- Generate variations of PDF outputs
- Export results in different formats
