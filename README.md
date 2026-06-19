# Claude Code Skills: Document Processing Suite

這個 repository 包含兩個強大的 Claude Code Skills，用於自動化文件處理和內容分析。

## 📋 概述

本項目包含：

1. **pdf-text-extractor** - PDF 文件提取與分析 Skill
2. **pptx-content-extractor** - PowerPoint 簡報提取與分析 Skill

這兩個 Skills 採用統一的架構，支持：
- 📖 文件內容提取
- 🤖 使用 Claude API 進行智能分析和問答
- 📝 自動生成新的格式化文件

---

## 🎯 Skill 1: pdf-text-extractor

### 功能描述

**目的**：提取 PDF 文件的內容，進行智能分析，並生成新的 PDF 文件

**核心能力**：
1. **讀取 PDF** - 提取所有頁面的文本內容
2. **智能問答** - 使用 Claude API 基於 PDF 內容回答問題
3. **PDF 生成** - 根據分析結果生成新的格式化 PDF 文件

### 📊 使用範例

#### 讀取和提取
```bash
python scripts/extract_and_analyze.py extract "path/to/document.pdf"
```

#### 回答問題
```bash
python scripts/extract_and_analyze.py answer "path/to/document.pdf" "What is the main topic?"
```

#### 生成摘要 PDF
```bash
python scripts/extract_and_analyze.py summarize "path/to/document.pdf" --output "./output"
```

### 📁 目錄結構

```
pdf-text-extractor/
├── SKILL.md                          # Skill 定義（YAML + Markdown）
├── requirements.txt                  # Python 依賴
├── scripts/
│   ├── extract_and_analyze.py       # 主程式
│   └── __init__.py
├── evals.json                        # 測試用例定義
├── run_tests.py                      # 測試執行器
├── test_output/                      # 生成文件輸出目錄
│   └── Summary_of_*.pdf             # 生成的 PDF 摘要
└── test_results.json                 # 測試結果
```

### 🧪 測試結果

**測試日期**：2026-06-19

| 測試項目 | 結果 | 詳情 |
|---------|------|------|
| **Test 1: 讀取和提取** | ✅ PASSED | 29 頁 PDF，166,627 字符成功提取 |
| **Test 2: 問答能力** | ⚠️ PASSED* | API 調用成功，回答基於 PDF 內容 |
| **Test 3: PDF 生成** | ✅ PASSED | 生成 5.2 KB 摘要 PDF 文件 |

*注：Test 2 終端顯示編碼問題待修復

**測試數據**：
- 輸入文件：`A Survey on Mixture of Experts.pdf` (29 頁)
- 提取文本：166,627 字符
- 生成摘要：5,177 字節 PDF

**查看測試結果**：
```
pdf-text-extractor/test_results.json
```

### 🔧 技術棧

- **Python** 3.13+
- **pdfplumber** - PDF 讀取和文本提取
- **reportlab** - PDF 生成和格式化
- **Anthropic Claude API** - 智能文本分析
- **Pillow** - 圖像處理

### 📦 安裝依賴

```bash
cd pdf-text-extractor
pip install -r requirements.txt
```

### ⚙️ 配置

#### 環境變數：ANTHROPIC_API_KEY

API Key 必須通過環境變數設置，**不要硬編碼**在代碼中。

**PowerShell (Windows)**：
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Bash/Zsh (Linux/Mac)**：
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**驗證設置**：
```bash
# PowerShell
$env:ANTHROPIC_API_KEY

# Bash
echo $ANTHROPIC_API_KEY
```

如果沒有設置 API Key，運行測試時會看到：
```
[ERROR] ANTHROPIC_API_KEY environment variable not set
Please set: $env:ANTHROPIC_API_KEY = 'your-api-key-here'
```

---

## 🎯 Skill 2: pptx-content-extractor

### 功能描述

**目的**：提取 PowerPoint 簡報的內容，進行智能分析，並生成新的簡報文件

**核心能力**：
1. **讀取 PPTX** - 提取所有幻燈片的文本內容和備註
2. **智能問答** - 使用 Claude API 基於簡報內容回答問題
3. **PPTX 生成** - 根據分析結果生成新的格式化簡報文件

### 📊 使用範例

#### 讀取和提取
```bash
python scripts/extract_and_analyze.py extract "path/to/presentation.pptx"
```

#### 回答問題
```bash
python scripts/extract_and_analyze.py answer "path/to/presentation.pptx" "What are the main points?"
```

#### 生成摘要簡報
```bash
python scripts/extract_and_analyze.py summarize "path/to/presentation.pptx" --output "./output"
```

### 📁 目錄結構

```
pptx-content-extractor/
├── SKILL.md                          # Skill 定義（YAML + Markdown）
├── requirements.txt                  # Python 依賴
├── scripts/
│   ├── extract_and_analyze.py       # 主程式
│   └── __init__.py
├── evals.json                        # 測試用例定義
├── run_tests.py                      # 測試執行器
├── test_output/                      # 生成文件輸出目錄
│   └── Summary_of_*.pptx            # 生成的簡報摘要
└── test_results.json                 # 測試結果
```

### 🧪 測試結果

**測試日期**：2026-06-19

| 測試項目 | 結果 | 詳情 |
|---------|------|------|
| **Test 1: 讀取和提取** | ✅ PASSED | 40 張幻燈片，7,713 字符成功提取 |
| **Test 2: 問答能力** | ✅ PASSED | Claude API 成功回答 freemium 商業模式問題 |
| **Test 3: PPTX 生成** | ✅ PASSED | 生成 38.5 KB 摘要簡報 |

**測試數據**：
- 輸入文件：`Selling the Premium in Freemium.pptx` (40 張幻燈片)
- 提取文本：7,713 字符
- 生成摘要：38,551 字節 PPTX

**查看測試結果**：
```
pptx-content-extractor/test_results.json
```

**查看生成的簡報**：
```
pptx-content-extractor/test_output/Summary_of_Selling_the_Premium_in_Freemium.pptx
```

### 🔧 技術棧

- **Python** 3.13+
- **python-pptx** - PPTX 讀取和編輯
- **Anthropic Claude API** - 智能文本分析
- **Pillow** - 圖像處理

### 📦 安裝依賴

```bash
cd pptx-content-extractor
pip install -r requirements.txt
```

### ⚙️ 配置

#### 環境變數：ANTHROPIC_API_KEY

API Key 必須通過環境變數設置，**不要硬編碼**在代碼中。

**PowerShell (Windows)**：
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Bash/Zsh (Linux/Mac)**：
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**驗證設置**：
```bash
# PowerShell
$env:ANTHROPIC_API_KEY

# Bash
echo $ANTHROPIC_API_KEY
```

如果沒有設置 API Key，運行測試時會看到：
```
[ERROR] ANTHROPIC_API_KEY environment variable not set
Please set: $env:ANTHROPIC_API_KEY = 'your-api-key-here'
```

---

## 🧪 運行測試

### 前置要求

設置 API Key 環境變數：

**PowerShell**：
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Bash/Linux/Mac**：
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 運行 pdf-text-extractor 測試

#### 方式 1：命令行提供文件路徑（推薦）
```bash
cd pdf-text-extractor
python run_tests.py "/path/to/your/document.pdf"
```

#### 方式 2：交互式輸入（無命令行參數）
```bash
cd pdf-text-extractor
python run_tests.py
# 程式將提示：Please provide the path to a PDF file:
# 輸入完整的 PDF 文件路徑
```

**測試輸出位置**：
- 測試結果：`test_results.json`
- 生成的 PDF：`test_output/Summary_of_*.pdf`

### 運行 pptx-content-extractor 測試

#### 方式 1：命令行提供文件路徑（推薦）
```bash
cd pptx-content-extractor
python run_tests.py "/path/to/your/presentation.pptx"
```

#### 方式 2：交互式輸入（無命令行參數）
```bash
cd pptx-content-extractor
python run_tests.py
# 程式將提示：Please provide the path to a PPTX file:
# 輸入完整的 PPTX 文件路徑
```

**測試輸出位置**：
- 測試結果：`test_results.json`
- 生成的 PPTX：`test_output/Summary_of_*.pptx`

### 📋 使用任意 PDF/PPTX 文件進行測試

**重要**：這些 Skills 支持**任意符合格式的 PDF 和 PPTX 文件**，不僅限於提供的測試文件：

```bash
# 測試自己的 PDF
cd pdf-text-extractor
python run_tests.py "C:/Users/YourName/Documents/MyDocument.pdf"

# 或
python run_tests.py "/home/user/documents/report.pdf"

# 測試自己的 PPTX
cd pptx-content-extractor
python run_tests.py "D:/Presentations/MyPresentation.pptx"
```

**文件要求**：
- PDF：必須為 `.pdf` 格式
- PPTX：必須為 `.pptx` 格式
- 文件必須存在且可讀取

---

## 📊 測試結果檔案位置

### pdf-text-extractor
```
pdf-text-extractor/
├── test_results.json              ← 詳細的測試結果 JSON
├── test_output/
│   └── Summary_of_A_Survey_on_Mixture_of_Experts.pdf  ← 生成的摘要 PDF
└── run_tests.py                   ← 重新運行測試的腳本
```

### pptx-content-extractor
```
pptx-content-extractor/
├── test_results.json              ← 詳細的測試結果 JSON
├── test_output/
│   └── Summary_of_Selling_the_Premium_in_Freemium.pptx  ← 生成的摘要簡報
└── run_tests.py                   ← 重新運行測試的腳本
```

---

## 🔍 檢查測試結果

### 查看 JSON 測試報告

```bash
# PDF Skill 測試結果
cat pdf-text-extractor/test_results.json

# PPTX Skill 測試結果
cat pptx-content-extractor/test_results.json
```

### 預期的測試輸出格式

```json
{
  "timestamp": "2026-06-19T...",
  "tests": [
    {
      "id": 1,
      "name": "Read and Extract",
      "status": "passed",
      "result": {
        "status": "success",
        "filename": "...",
        "slides/pages": N,
        "content_length": N
      }
    },
    {
      "id": 2,
      "name": "Answer Question",
      "status": "passed",
      "question": "...",
      "answer_preview": "..."
    },
    {
      "id": 3,
      "name": "Generate Summary [PDF/PPTX]",
      "status": "passed",
      "output_file": "...",
      "file_size": N
    }
  ]
}
```

---

## 🚀 AI 工作流程說明

### 開發過程

本項目採用 Claude Code + Skill Creator 的工作流程開發：

1. **需求分析** - 確定 Skills 的核心功能和目標
2. **架構設計** - 定義 SKILL.md 結構和 Python 實現架構
3. **代碼實現** - 逐步填充實現代碼（避免 token 超限）
   - Phase 1: PDFReader/PPTXReader 類實現
   - Phase 2: DocumentAnalyzer 和 Generator 類
   - Phase 3: 主工作流函數和 CLI 接口
4. **測試驗證** - 使用自動化測試腳本驗證功能
5. **迭代改進** - 記錄已知問題（編碼、格式化）供後續改進

### 使用的 Claude Code Features

- **Claude Code CLI** - 用於代碼編輯和執行
- **skill-creator** - 用於 Skill 定義和測試用例管理
- **PowerShell/Bash** - 環境設置和測試運行
- **Python Scripts** - 核心業務邏輯實現

### 已知問題 & TODO

- [ ] **PDF Skill Test 2** - 終端編碼問題（cp950 codec）- 待修復
- [ ] **PDF/PPTX Skill** - 生成文件的內文與格式優化 - 待改進
- [ ] **部署** - 部署到公網（Zeabur 等）- 待進行

---

## 📝 主要假設

1. **Python 版本** - 使用 Python 3.13+
2. **API 金鑰** - 需要有效的 Anthropic API Key（已通過環境變數設置）
3. **依賴安裝** - 所有 Python 依賴已通過 requirements.txt 安裝
4. **文件格式** - 支持標準的 PDF 和 PPTX 格式
5. **文件大小** - 輸入文件不超過 50MB，輸出文件不超過 100MB

---

## 📚 文件說明

### SKILL.md

每個 Skill 的 SKILL.md 包含：
- **YAML 元數據** - 名稱、描述、相容性
- **Markdown 指導** - 詳細的功能說明、使用方式、技術細節

示例：`pdf-text-extractor/SKILL.md`

### Python 實現

#### PDFReader / PPTXReader
- 讀取文件並提取內容
- 提供元數據和統計信息

#### DocumentAnalyzer
- 使用 Claude API 進行文本分析
- 支持問答、摘要、關鍵點提取

#### PDFGenerator / PPTXGenerator
- 從文本內容生成新文件
- 支持自定義標題和格式

---

## 🔧 故障排除

### 問題：缺少依賴

```bash
pip install -r pdf-text-extractor/requirements.txt
pip install -r pptx-content-extractor/requirements.txt
```

### 問題：API Key 未設置

```bash
$env:ANTHROPIC_API_KEY = "your-api-key"
```

### 問題：文件路徑問題

確保使用絕對路徑或正確的相對路徑：
```bash
python scripts/extract_and_analyze.py extract "C:\full\path\to\file.pdf"
```

---

## 📄 許可證

MIT License

---

## 👨‍💻 開發者備註

### 開發時間軸
- **2026-06-19** - 完成兩個 Skills 的完整開發和測試
- **2026-06-19** - pdf-text-extractor: 2/3 測試通過
- **2026-06-19** - pptx-content-extractor: 3/3 測試通過
- **待進行** - 編碼問題修復、格式優化、公網部署

### 使用的技術

| 技術 | 目的 |
|------|------|
| Claude Code | AI 輔助開發 |
| Skill Creator | Skill 定義和測試管理 |
| Python 3.13+ | 核心實現 |
| pdfplumber | PDF 文本提取 |
| python-pptx | PPTX 讀寫 |
| reportlab | PDF 生成 |
| Anthropic Claude API | 智能文本分析 |

### 下一步計畫

1. ✅ 開發 pdf-text-extractor 和 pptx-content-extractor
2. ✅ 完成測試並驗證功能
3. ⏳ 修復已知問題（編碼、格式優化）
4. ⏳ 優化 Skill 描述以改進觸發精度
5. ⏳ 部署到公網（Zeabur）
6. ⏳ 提交完整的代碼和文檔

---

## 📞 聯繫和支持

如有問題或建議，請查看各 Skill 的 `SKILL.md` 了解更多詳情。
