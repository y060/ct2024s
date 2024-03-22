import argparse

# 使用 argparse 解析命令行參數
parser = argparse.ArgumentParser(description="Process input and output filenames.")
parser.add_argument("-i", "--input", required=True, help="Input file name")
parser.add_argument("-o", "--output", required=True, help="Output file name")
args = parser.parse_args()

# 讀取輸入檔案
with open(args.input, "r", encoding="utf-8") as file:
    text = file.read()

# 去除空格和換行符
text = text.replace(" ", "").replace("\n", "")

# 使用集合（set）來取得不重複的字符
unique_characters = set(text)

# 建立一個txt檔案並將不重複的字元寫入其中
output_file = args.output
with open(output_file, "w", encoding="utf-8") as file:
    for char in unique_characters:
        file.write(char)

# 計算不重複字元的數量
count = len(unique_characters)
print("不重複字符的数量:", count)
print(f"不重複的字符已保存到 {output_file}")
