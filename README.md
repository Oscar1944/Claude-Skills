# Claude Code Skills: Document Processing Suite

兩個強大的 Claude Code Skills，用於智能處理和分析 PDF 和 PowerPoint 文件。

## 📖 概述

本項目包含：

1. **pdf-text-extractor** - 智能 PDF 文件提取與分析
2. **pptx-content-extractor** - 智能 PowerPoint 簡報提取與分析

### 核心功能

無論是哪個 Skill，都能：
- 🔖 **讀取文件** - 提取 PDF/PPTX 中的所有內容
- 💭 **智能問答** - 基於文件內容回答您的問題（由 Claude AI 驅動）
- 📄 **生成文件** - 根據分析結果生成新的 PDF/PPTX

---

## 🚀 在 Claude 中使用 Skills

### 安裝 Skills 到 Claude

#### 步驟 1：找到 Skills 目錄

在您的 Claude 安裝位置找到 Skills 目錄：

**Windows：**
```
%APPDATA%\Claude\plugins\cache\claude-plugins-official\skill-creator\unknown\skills\
```

**Mac/Linux：**
```
~/.claude/plugins/cache/claude-plugins-official/skill-creator/unknown/skills/
```

#### 步驟 2：安裝 Skills

將 `pdf-text-extractor` 和 `pptx-content-extractor` 文件夾複製到上述 Skills 目錄。

#### 步驟 3：安裝依賴（Claude 會自動執行）

當您首次使用 Skill 時，Claude 會自動檢測並安裝所需的 Python 包：

- **pdf-text-extractor** 需要：
  - `pdfplumber` - PDF 讀取
  - `reportlab` - PDF 生成

- **pptx-content-extractor** 需要：
  - `python-pptx` - PPTX 讀寫

### 設置 API Key

Skills 需要 Anthropic API Key。在 Claude 中設置環境變數：

```
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

---

## 📚 使用 Skills

### pdf-text-extractor

#### 功能

✅ 讀取任意 PDF 文件並提取內容  
✅ 根據 PDF 內容回答問題  
✅ 生成摘要或分析報告為新 PDF  

#### 使用方式

直接在 Claude 中詢問：

```
"讀取我的 PDF 文件並總結主要內容"
"根據這個 PDF，什麼是稀疏 MoE（Sparse MoE）？"
"從這個 PDF 生成一份摘要 PDF"
```

Claude 會自動：
1. 提示您提供 PDF 文件的路徑
2. 讀取並分析文件
3. 提供答案或生成新文件

### pptx-content-extractor

#### 功能

✅ 讀取任意 PPTX 簡報並提取所有幻燈片內容  
✅ 根據簡報內容回答問題  
✅ 生成新簡報或摘要簡報  

#### 使用方式

直接在 Claude 中詢問：

```
"讀取我的 PowerPoint 簡報並提取關鍵要點"
"根據這個簡報，主要的業務優勢是什麼？"
"從這個簡報生成一份精簡版本"
```

Claude 會自動：
1. 提示您提供 PPTX 文件的路徑
2. 讀取所有幻燈片
3. 提供答案或生成新文件

---

## 🧪 測試驗證

### pdf-text-extractor 測試結果

✅ **所有測試通過** (3/3)

| 測試 | 結果 | 詳情 |
|------|------|------|
| **Test 1: 讀取和提取** | ✅ PASSED | 29 頁，166,627 字符成功提取 |
| **Test 2: 問答能力** | ✅ PASSED | Claude API 成功基於文件內容回答問題 |
| **Test 3: PDF 生成** | ✅ PASSED | 成功生成 5 KB 摘要 PDF 文件 |

**更新時間：** 2026-06-19  
**測試數據：** A Survey on Mixture of Experts.pdf (29 頁，學術論文)

### pptx-content-extractor 測試結果

✅ **所有測試通過** (3/3)

| 測試 | 結果 | 詳情 |
|------|------|------|
| **Test 1: 讀取和提取** | ✅ PASSED | 40 張幻燈片，7,713 字符成功提取 |
| **Test 2: 問答能力** | ✅ PASSED | Claude API 成功基於簡報內容回答問題 |
| **Test 3: PPTX 生成** | ✅ PASSED | 成功生成 38.5 KB 摘要簡報 |

**更新時間：** 2026-06-19  
**測試數據：** Selling the Premium in Freemium.pptx (40 張幻燈片，商業簡報)

---

## 💡 使用案例

### PDF Skill

- 📖 分析學術論文並提取關鍵概念
- 📊 從報告中提取數據和統計信息
- 💼 理解商業文檔和合同條款
- 🎓 學習和復習教科書內容
- 📝 快速生成文檔摘要

### PPTX Skill

- 🎤 理解演講主題和要點
- 📈 分析商業或營銷簡報
- 🎓 總結教學演示文稿
- 💡 提取創意和想法
- 📋 從簡報生成會議筆記

---

## ⚙️ 系統要求

- **Python** 3.10 或更高
- **Claude Code** 或 **Claude.ai** (支持 Skill)
- **有效的 Anthropic API Key**

## 📋 支援的文件格式

- **PDF**: 標準 PDF 文件
- **PPTX**: Microsoft PowerPoint 2007 及以上版本

---

## 🎯 快速開始

### 場景 1：第一次使用

```
您（在 Claude 中）: "我想用 pdf-text-extractor Skill 讀取一份 PDF"

Claude: "我會幫您讀取 PDF。請提供 PDF 文件的完整路徑。"

您: "C:/Users/MyName/Documents/research_paper.pdf"

Claude: [自動安裝依賴] [讀取文件] [提供分析]
```

### 場景 2：回答基於文檔的問題

```
您: "基於我的 PDF，主要的研究成果是什麼？"

Claude: [自動讀取您提供的文件] [分析內容] [提供基於文件的回答]
```

### 場景 3：生成新文件

```
您: "從這個 PowerPoint 生成一份精簡摘要簡報"

Claude: [讀取簡報] [分析內容] [生成新 PPTX] [提供文件位置]
```

---

## 🔒 安全性

- API Keys 通過環境變數安全管理
- 文件處理完全本地化
- 沒有數據永久存儲
- 支持任意格式的 PDF 和 PPTX 文件（不限於示例文件）

---

## 📝 授權

MIT License

---

## 需要幫助？

如果 Skill 不工作：

1. **檢查 API Key 是否已設置**
   ```
   $env:ANTHROPIC_API_KEY
   ```

2. **驗證文件路徑**
   - 確保文件存在
   - 使用完整路徑而非相對路徑

3. **確認文件格式**
   - PDF Skill：確保是 `.pdf` 格式
   - PPTX Skill：確保是 `.pptx` 格式

4. **檢查 Python 版本**
   - 需要 Python 3.10 或更高

如果問題持續，請在 Claude 中詢問，它會幫您診斷和解決問題。
