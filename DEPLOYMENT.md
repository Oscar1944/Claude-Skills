# 部署指南 - Document Extraction Web Service

本文檔說明如何在本地運行和部署 Document Extraction API 到 Zeabur。

## 📋 目錄

1. [本地開發](#本地開發)
2. [Zeabur 部署](#zeabur-部署)
3. [配置 Claude Skills](#配置-claude-skills)
4. [API 使用](#api-使用)

---

## 本地開發

### 前置要求

- Python 3.10 或更高
- pip（Python 套件管理器）

### 步驟 1：安裝依賴

```bash
cd Claude-Skills
pip install -r requirements.txt
```

### 步驟 2：執行 API 伺服器

```bash
python main.py
```

伺服器將在 `http://localhost:8000` 啟動

### 步驟 3：驗證 API

訪問 `http://localhost:8000` 查看健康檢查和可用端點

```bash
curl http://localhost:8000
```

### 步驟 4：測試提取功能

**測試 PDF 提取：**
```bash
curl -X POST -F "file=@/path/to/test.pdf" http://localhost:8000/extract-pdf
```

**測試 PPTX 提取：**
```bash
curl -X POST -F "file=@/path/to/test.pptx" http://localhost:8000/extract-pptx
```

---

## Zeabur 部署

### 前置要求

- [Zeabur 帳號](https://zeabur.com)
- Git

### 步驟 1：推送到 GitHub

確保您的 `Claude-Skills` 項目已推送到 GitHub

### 步驟 2：在 Zeabur 連接倉庫

1. 訪問 https://dash.zeabur.com
2. 點擊 "New Project"
3. 選擇 "Deploy from Git"
4. 連接您的 GitHub 帳號
5. 選擇 `Claude-Skills` 倉庫

### 步驟 3：配置環境

Zeabur 將自動檢測 Python 項目。確保：
- 根目錄有 `requirements.txt` ✓
- 根目錄有 `Procfile` ✓
- 設置環境變數（如需要）：
  ```
  PORT=8000
  ```

### 步驟 4：部署

點擊 "Deploy" 按鈕。Zeabur 將自動：
1. 檢測 Python 項目
2. 安裝依賴
3. 使用 `Procfile` 啟動伺服器

### 步驟 5：獲取部署 URL

部署完成後，您會得到一個公網 URL，例如：
```
https://your-project.zeabur.app
```

---

## 配置 Claude Skills

### 使用本地 API

1. 確保本地 API 伺服器在運行：
   ```bash
   python main.py
   ```

2. Skills 會自動連接到 `http://localhost:8000`

### 使用 Zeabur 部署的 API

1. 在 Claude 中設置環境變數：
   ```
   $env:PDF_EXTRACTION_API_URL = "https://your-project.zeabur.app"
   $env:PPTX_EXTRACTION_API_URL = "https://your-project.zeabur.app"
   ```

2. 或者編輯 Skills 的 `api_client.py`：
   ```python
   # 修改預設 API URL
   client = PDFExtractionAPIClient(api_url="https://your-project.zeabur.app")
   ```

---

## API 使用

### 端點 1：PDF 提取

**URL：** `POST /extract-pdf`

**請求：**
```bash
curl -X POST \
  -F "file=@document.pdf" \
  http://localhost:8000/extract-pdf
```

**響應：**
```json
{
  "status": "success",
  "filename": "document.pdf",
  "pages": 29,
  "text_length": 166627,
  "preview": "text preview..."
}
```

### 端點 2：PPTX 提取

**URL：** `POST /extract-pptx`

**請求：**
```bash
curl -X POST \
  -F "file=@presentation.pptx" \
  http://localhost:8000/extract-pptx
```

**響應：**
```json
{
  "status": "success",
  "filename": "presentation.pptx",
  "slides": 40,
  "content_length": 7713,
  "preview": "text preview..."
}
```

### 健康檢查

**URL：** `GET /`

```bash
curl http://localhost:8000
```

---

## 故障排除

### 連接被拒絕

**問題：** `Cannot connect to API at http://localhost:8000`

**解決方案：**
1. 確保 `python main.py` 在運行
2. 檢查防火牆設置
3. 驗證端口 8000 沒有被佔用：`netstat -an | grep 8000`

### 模塊導入錯誤

**問題：** `ModuleNotFoundError: No module named 'extract_and_analyze'`

**解決方案：**
1. 確保安裝了所有依賴：`pip install -r requirements.txt`
2. 檢查 Python 路徑設置
3. 確保在根目錄執行 `python main.py`

### 文件上傳失敗

**問題：** `File must be a PDF/PPTX`

**解決方案：**
1. 確保文件副檔名正確（.pdf 或 .pptx）
2. 檢查文件是否損壞
3. 驗證文件大小不超過伺服器限制

---

## 性能優化建議

1. **快取結果** - 考慮快取已提取的文檔
2. **非同步處理** - FastAPI 已是非同步的
3. **負載均衡** - 在 Zeabur 中可配置多個副本
4. **文件大小限制** - 考慮在 `main.py` 中添加大小驗證

---

## 下一步

- 添加身份驗證（API Key）
- 實現文件快取機制
- 添加更多端點（生成 PDF/PPTX、問答等）
- 設置監控和日誌
