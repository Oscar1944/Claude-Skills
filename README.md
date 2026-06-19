# Claude Code Skills: Document Processing Suite

兩個 Claude Code Skills，用於處理 PDF 和 PowerPoint 文件。

---

## 🚀 Quick Start

### 步驟 1：安裝 Skills

將 `pdf-text-extractor` 和 `pptx-content-extractor` 兩個資料夾複製到 Claude Code 的 Skills 目錄：

**Windows：**
```
%APPDATA%\Claude\plugins\cache\claude-plugins-official\skill-creator\unknown\skills\
```

**Mac/Linux：**
```
~/.claude/plugins/cache/claude-plugins-official/skill-creator/unknown/skills/
```

### 步驟 2：安裝 Python 套件

Claude 會在首次使用 Skill 時自動安裝所需套件，無需手動操作。

若需要手動安裝（如執行測試）：

```bash
pip install anthropic reportlab python-pptx requests
```

### 步驟 3：設定 API Key

```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "your-api-key-here"

# Mac/Linux
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 步驟 4：開始使用

在 Claude Code 中直接描述需求即可，例如：

```
讀取 report.pdf 並產生 100 字摘要
```
```
把 slides.pptx 的內容整理後輸出成新的簡報
```
```
清理這份 PDF 的內容，移除特殊符號後存成新的 PDF
```

> **不需要自己架設任何服務。** 文件內容提取由雲端 API（`https://claude-skill.zeabur.app`）處理，Skills 會自動呼叫。

---

## 架構說明

```
使用者 → Claude Skill → FastAPI Web Service → 回傳文件內容 → Claude 進一步處理
```

Skills 本身**不**在本地解析文件。文件內容的提取由部署在 Zeabur 的 FastAPI Web Service 負責（`https://claude-skill.zeabur.app`），Skill 透過 API 取得內容後，再由 Claude 進行分析、摘要、問答等工作。

---

## 包含的 Skills

### 1. pdf-text-extractor

讀取 PDF 文件，能夠：
- 產生摘要
- 修改/清理文件內容
- 輸出為新的 PDF 文件

### 2. pptx-content-extractor

讀取 PowerPoint 簡報，能夠：
- 產生摘要
- 修改/清理投影片內容
- 輸出為新的 PPTX 文件

---

## Web Service

文件內容提取由 FastAPI 服務處理，已部署於 `https://claude-skill.zeabur.app`。

若需要自行部署，在 Zeabur 連接此 GitHub 倉庫即可自動建置（已包含 `Dockerfile`）。

| 端點 | 說明 |
|------|------|
| `POST /extract-pdf` | 上傳 PDF，回傳文字內容與 metadata |
| `POST /extract-pptx` | 上傳 PPTX，回傳投影片內容與 metadata |

---

## 測試

### 執行測試

```bash
# PDF skill
python3 pdf-text-extractor/run_tests.py "path/to/document.pdf"

# PPTX skill
python3 pptx-content-extractor/run_tests.py "path/to/presentation.pptx"
```

### 測試項目

兩個 Skill 各有 3 項測試：

| 測試 | 說明 |
|------|------|
| Test 1 | 產生 100 字摘要（驗證 Skill 能讀到文件內容）|
| Test 2 | 修改文件內容（驗證 Skill 能清理/編輯內容）|
| Test 3 | 輸出檔案（驗證 Skill 能將結果存成 PDF/PPTX）|

### 最新測試結果（2026-06-20）

**pdf-text-extractor** — 測試資料：A Survey on Mixture of Experts.pdf（29 頁）

| 測試 | 結果 |
|------|------|
| Test 1: 產生摘要 | ✅ PASSED（103 字）|
| Test 2: 修改內容 | ✅ PASSED（166,172 → 164,432 字元）|
| Test 3: 輸出 PDF | ✅ PASSED（3,396 bytes）|

**pptx-content-extractor** — 測試資料：Selling the Premium in Freemium.pptx（40 張）

| 測試 | 結果 |
|------|------|
| Test 1: 產生摘要 | ✅ PASSED（93 字）|
| Test 2: 修改內容 | ✅ PASSED（提取 40 張投影片標題）|
| Test 3: 輸出 PPTX | ✅ PASSED（31,525 bytes）|

---

## License

MIT
