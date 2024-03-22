# script_ntut

### 製作包含 CP950 所有字元稿紙

![GITHUB](https://github.com/Circle472/script_ntut/raw/main/scripts_pku_file.jpg)

### 安裝 requirements.txt 套件
```
pip install –r requirements.txt
```

### 修改 info.py 程式碼
```python
TOTAL_PAGES = 138
# personal information below
ID = "STUDENT_ID"  # enter your ID here
NAME = "NAME_HERE"  # enter your name here
NUMBER = 0  # enter your number here
```

### 執行程式碼
#### 步驟一：生成 138 張 svg 稿紙
```
python 1_SVGtable.py
```
#### 步驟二：將 138 張 svg 檔案加上 QRcode
```
python 2_QR_add.py
```
#### 步驟三：將 138 張 svg 轉成 138 個 pdf 檔案
```
python 3_SVG2PDF.py
```
#### 步驟四：將 138 張 pdf 檔案合併成一個 pdf 檔案
```
python 4_PDFmerge.py
```
![GITHUB](https://github.com/Circle472/script_ntut/raw/main/scripts_pku_intro.jpg)
