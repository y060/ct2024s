with open("all_word.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 去除空格和換行符
text = text.replace(" ", "").replace("\n", "")

# 使用集合（set）來取得不重複的字符
unique_characters = set(text)

# 建立一個txt檔案並將不重複的字元寫入其中
output_file = "chinese_character.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for char in unique_characters:
        file.write(char)

# 計算不重複字元的數量
count = len(unique_characters)
print("不重複字符的数量:", count)
print(f"不重複的字符已保存到 {output_file}")
