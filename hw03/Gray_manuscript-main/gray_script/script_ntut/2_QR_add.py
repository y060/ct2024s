# ADD_QRCODE
import info
import os
import qrcode
import qrcode.image.svg
from xml.etree import ElementTree as ET

# 創建存儲 QR Code 的資料夾
qrcode_folder = "./qrcode"
os.makedirs(qrcode_folder, exist_ok=True)

for i in range(info.TOTAL_PAGES):
    # 讀取原本的 SVG 檔案
    with open(f"./Table/{i+1:03d}.svg", "rb") as file:
        svg_content = file.read()

    # 產生 QR Code 圖片
    factory = qrcode.image.svg.SvgPathImage
    qr_code = qrcode.make(i+1, image_factory=factory)

    # 將 QR Code 存成檔案
    qr_code.save(f"{qrcode_folder}/qrcode_{i+1:03d}.svg")

    # 讀取 QR Code SVG 檔案
    with open(f"{qrcode_folder}/qrcode_{i+1:03d}.svg", "rb") as qr_file:
        qr_code_svg_str = qr_file.read().decode('utf-8')

    # 找到最後一個 </svg> 標籤的位置
    last_svg_index = svg_content.rfind(b'</svg>')

    # 在最後一個 </svg> 之前插入 QR Code SVG 字串，並加入 transform 屬性
    updated_svg_content = (
        svg_content[:last_svg_index].decode('utf-8') +
        f'<g transform="translate(498,772) scale(0.6)">{qr_code_svg_str[qr_code_svg_str.find("<svg"):].strip()}</g>'
        + svg_content[last_svg_index:].decode('utf-8')
    )

    # 將更新後的 SVG 寫回檔案
    with open(f"Merge/{i+1:03d}.svg", "wb") as file:
        file.write(updated_svg_content.encode('utf-8'))

print("QR Code 已成功插入 SVG 中")
