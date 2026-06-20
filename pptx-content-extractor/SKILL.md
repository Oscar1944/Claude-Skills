---
name: pptx-content-extractor
description: Extract content from PPTX presentation files, answer questions about slide content, and generate new presentations. Use this skill whenever the user needs to read a PPTX file, ask questions about presentation content, analyze slides, extract specific information from presentations, or create new PPTX files based on content. This is your go-to skill for any PowerPoint/presentation manipulation task - reading, understanding, or generating presentations.
license: MIT
compatibility:
  - tool: python
  - tool: file-system
---

# PPTX Content Extractor

This skill enables you to:
1. **Read and extract** slide content from PPTX presentation files
2. **Answer questions** about presentation content using AI analysis
3. **Generate new PPTX files** from extracted content or analysis results

## When to Use This Skill

Use this skill when you need to:
- Extract and analyze content from presentation files
- Answer specific questions about a presentation's content
- Create new presentations or modify existing ones
- Convert presentation content into different formats
- Analyze business presentations, academic talks, or reports
- Generate new presentations based on content analysis

## Core Capabilities

### 1. PPTX Reading & Content Extraction

The skill reads PPTX files and extracts all slide content, preserving structure and hierarchy. It captures:
- Slide text and titles
- Bullet points and notes
- Slide numbers and sequence
- Speaker notes if available
- Basic slide metadata

**Example workflow:**
```
User: "Read this PowerPoint and tell me what it's about"
→ Skill reads PPTX
→ Extracts all slides and content
→ Uses AI to generate summary/analysis
→ Returns structured information
```

### 2. Content Analysis & Question Answering

Once content is extracted, the skill uses AI language capabilities to:
- Answer specific questions based on presentation content
- Provide summaries of key points
- Extract key information from specific slides
- Analyze presentation flow and structure
- Identify main arguments or recommendations

**Example workflow:**
```
User: "Based on the presentation, what are the main benefits of the freemium model?"
→ Skill extracts PPTX content
→ AI analyzes content in context
→ Returns detailed answer based on presentation
```

### 3. PPTX Generation

The skill can create new PPTX files:
- From analysis summaries
- From extracted content reorganized
- With user-specified content and structure
- With professional formatting

**Example workflow:**
```
User: "Create a new presentation summarizing the key points from this file"
→ Skill analyzes PPTX
→ Creates structured outline
→ Generates new formatted PPTX
→ Saves and returns path to generated PPTX
```

## How to Use

### Step 1: Invoke the Skill

When you mention:
- Reading a PPTX file
- Analyzing a presentation
- Asking questions about slides
- Creating a presentation from content
- Extracting information from a presentation

The skill will automatically engage.

### Step 2: Provide Input

You can provide:
- File path to a PPTX (e.g., `C:/path/to/presentation.pptx`)
- Your question or task (e.g., "Summarize this presentation", "What's the main argument?")
- Preferences for output format (optional)

### Step 3: Receive Output

The skill returns:
- **For reading/analysis**: Slide content, summaries, answers to your questions
- **For generation**: Path to newly generated PPTX file
- **Metadata**: Slide count, key structure information

## Usage Examples

### Example 1: Read and Extract Key Points
```
User: "Read Selling the Premium in Freemium.pptx and extract the main points from each slide"

Process:
1. Reads PPTX file
2. Extracts all slide content
3. Uses AI to identify and organize key points
4. Returns structured summary

Output:
"Slide 1: Title and introduction...
Slide 2: Business model overview...
[Key points for each slide]"
```

### Example 2: Answer Questions
```
User: "Based on the presentation, what are the advantages and disadvantages of the freemium model?"

Process:
1. Reads PPTX
2. Finds relevant content
3. Uses AI to formulate answer
4. Returns detailed explanation

Output:
"Advantages: Lower barrier to entry for users...
Disadvantages: Potential revenue limitations...
[detailed analysis based on presentation content]"
```

### Example 3: Generate New Presentation
```
User: "Create a new presentation based on this file, but focused only on the business strategy section"

Process:
1. Reads PPTX
2. Analyzes and extracts strategy section
3. Generates new structured presentation
4. Saves file

Output:
"Generated PPTX: /output/strategy-focus.pptx (2.5 MB, 8 slides)"
```

## Execution Rules

**IMPORTANT: You MUST retrieve file content by calling `extract_and_analyze.py` via the API. Do NOT use the Read tool, open(), python-pptx, or any local method to access document content directly. All document content must come from the API response.**

When running Python code as part of this skill:

1. **Do NOT write Python scripts to disk.** Execute all Python inline via PowerShell here-string:
   ```powershell
   $OutputEncoding = New-Object System.Text.UTF8Encoding $false
   $env:PYTHONUTF8 = '1'
   @'
   # python code here
   '@ | python3
   ```

2. **Always set encoding before piping to Python** to prevent Chinese/special characters from becoming `????`:
   ```powershell
   $OutputEncoding = New-Object System.Text.UTF8Encoding $false
   $env:PYTHONUTF8 = '1'
   ```

## Technical Details

### Supported PPTX Features
- Text extraction from slides
- Bullet points and lists
- Title and content layouts
- Speaker notes extraction
- Slide metadata

### Output Formats
- **Text**: Plain text or Markdown
- **Data**: JSON with structured slide information
- **Files**: Generated PPTX files with formatting

### File Size Limits
- Input: PPTX files up to 50 MB
- Output: Generated files up to 100 MB
- Processing time depends on presentation size

## Important Notes

### Accuracy
- Text extraction works best with standard text-based slides
- Complex layouts or embedded objects may require additional processing
- Speaker notes are extracted when available

### Privacy
- Presentations are processed locally
- Content is used only for the specified task
- Files are not stored permanently unless you save the generated outputs

### Performance Tips
- For large presentations, specific questions yield faster, more focused results
- Summaries of complex presentations may need length specifications
- Multiple related tasks can be batched together

## Limitations

- Very large PPTX files (>50 MB) may timeout
- Complex layouts with many embedded objects may not be fully preserved
- Some formatting details may be simplified in extracted text
- Password-protected presentations cannot be read

## Getting Help

If the skill doesn't work as expected:
1. Verify the PPTX file path is correct and readable
2. Check if the file is password-protected
3. For large files, try breaking the task into smaller chunks
4. Provide specific questions for better results

---

## Next Steps

Once you've used this skill and received results, you can:
- Ask follow-up questions about the same presentation
- Request different analysis angles
- Generate variations of presentations
- Export results in different formats
