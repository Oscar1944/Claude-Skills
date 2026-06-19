# Claude Code Skills: Document Processing Suite

兩個 Claude Code Skills，用於處理 PDF 和 PowerPoint 文件。

## 架構說明

```
使用者 → Claude Skill → FastAPI Web Service → 回傳文件內容 → Claude 進一步處理
```

Skills 本身**不**在本地解析文件。文件內容的提取由 FastAPI Web Service 負責，Skill 透過 API 取得內容後，再由 Claude 進行分析、摘要、問答等工作。

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

## 部署 Web Service

Skills 依賴一個 FastAPI Web Service 來提取文件內容，需要先啟動它。

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 啟動服務（本地）

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 部署到 Zeabur

推送到 GitHub 後，在 Zeabur 連接倉庫即可自動部署（已包含 `Procfile`）。

### API 端點

| 端點 | 方法 | 說明 |
|------|------|------|
| `/extract-pdf` | POST | 上傳 PDF，回傳文字內容與 metadata |
| `/extract-pptx` | POST | 上傳 PPTX，回傳投影片內容與 metadata |

---

## 使用 Skills

在 Claude Code 中直接描述需求即可：

```
"讀取 report.pdf 並產生 100 字摘要"
"把 slides.pptx 的內容整理後輸出成新的簡報"
"清理這份 PDF 的內容，移除特殊符號後存成新的 PDF"
```

**前置條件：**
- FastAPI Web Service 需要在運行中
- 若需要 Claude API 獨立呼叫（如執行測試），需設定 `ANTHROPIC_API_KEY`

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
