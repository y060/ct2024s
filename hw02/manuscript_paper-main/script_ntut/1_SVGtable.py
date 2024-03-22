# -*- coding: utf-8 -*-
import json
import numpy as np
from tqdm import tqdm
import multiprocessing as mp
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

import info

plt.rcParams["font.sans-serif"] = ["mingliu"]  # font family: '細明體MingLiU'
plt.rcParams["axes.unicode_minus"] = False

AMOUNT = 1186

def decimal_to_binary(number, digits):
    index = digits - 1
    binaries = [0] * digits
    while number > 0:
        binaries[index] = number % 2  # True / False
        index -= 1
        number >>= 1
    return binaries  # list of booleans


def create_plot(page):
    # figure
    fig = plt.figure(
        num=page, figsize=(8.27, 11.69), dpi=72, facecolor="white"
    )  # figure size (inches)
    axes = plt.subplot(111)

    plt.text(120, 7, "字體設計與文字編碼", fontsize=12.5, color="black")
    student = info.ID + "_" + info.NAME
    plt.text(70, 7, student, fontsize=12.5, color="black")
    number = info.NUMBER

    table_square(axes)

    # page number
    temp_page = page + 1

    plt.text(
        175,
        7,
        "第 {}/{} 頁".format(temp_page, info.TOTAL_PAGES),
        fontsize=12.5,
        color="black",
    )
    plt.text(
        10,
        8,
        "字順 {}-{}".format(100 * (temp_page - 1) + 1, 100 * temp_page),
        fontsize=17,
        color="black",
    )
    plt.text(88, 285, "頁碼", fontsize=11, color="black")
    rect = patches.Rectangle(
        (98, 279), 58, 9, linewidth=1, edgecolor="black", facecolor="black", fill=False
    )
    axes.add_patch(rect)
    plt.text(158, 285, str(temp_page), fontsize=11, color="black")

    # decimal to binary
    binaries = decimal_to_binary(temp_page, 8)

    # square
    for j, fill in enumerate(binaries):
        rect = patches.Rectangle(
            (100 + 7 * j, 281),
            5,
            5,
            linewidth=1,
            edgecolor="black",
            facecolor="black",
            fill=fill,
        )
        axes.add_patch(rect)

    plt.text(8, 285, "編號", fontsize=11, color="black")
    rect = patches.Rectangle(
        (18, 279), 58, 9, linewidth=1, edgecolor="black", facecolor="black", fill=False
    )
    axes.add_patch(rect)
    plt.text(78, 285, str(number), fontsize=11, color="black")

    # decimal to binary
    binaries = decimal_to_binary(number, 8)

    # number square
    for j, fill in enumerate(binaries):
        rect = patches.Rectangle(
            (20 + 7 * j, 281),
            5,
            5,
            linewidth=1,
            edgecolor="black",
            facecolor="black",
            fill=fill,
        )
        axes.add_patch(rect)


# def read_json(file):
#     with open(file) as f:
#         p = json.load(f)
#         v = [""] * 763
#         for i in range(763):
#             # 128 - 255: 'UNICODE' = '     '; 0 - 31: unable to print
#             # if (128 <= i & i < 256) or (0 <= i & i < 32):
#             #     v[i] = "123"
#             # else:
#                 code = p["CP950"][i]["UNICODE"][2:6]
#                 v[i] = "\\u{}".format(code)  # ex: 0x1234 --> \\u1234      
#         return v

def read_json(file):
    with open(file) as f:
        try:
            p = json.load(f)
        except UnicodeDecodeError:
            # Handle the UnicodeDecodeError here (e.g., print a message, log it, or skip the file).
            print(f"Error reading JSON file: {file}")
            return []
        
        v = [""] * AMOUNT
        for i in range(AMOUNT):
            try:
                code = p["CP950"][i]["UNICODE"][2:6]
                v[i] = "\\u{}".format(code)
            except Exception as e:
                # Handle the exception here (e.g., print a message, log it, or skip the entry).
                print(f"Error processing entry {i}: {str(e)}")
                v[i] = ""  # You can decide what to do in case of an error.
        return v

def print_font(count, page, fnip):
    index = 0
    X = np.arange(7.5, 192.5, 20)
    Y = np.arange(21, 281, 26)
    for j in range(10):
        for i in range(10):
            if count >= AMOUNT:
                plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
                # plt.text(12.5+16.25*j, 23+17*i, '', fontsize=32, color='black')
            else:
                if unicode[count] == "123" or count >= AMOUNT:
                    plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
                    fnip[page][index] = ""  # 第(page+1)頁 第(index+1)個字
                    # plt.text(7+16.25*j, 26.7+17*i, '\\u25A0'.encode('ascii').decode('unicode-escape'), fontsize=64, color='black')
                else:
                    plt.text(
                        X[i] + 1,
                        Y[j] - 3,
                        unicode[count].encode("ascii").decode("unicode-escape"),
                        fontsize=14,
                        color="black",
                        alpha=0.7,
                    )
                    plt.text(
                        X[i] + 8.5,
                        Y[j] - 3,
                        unicode[count][2:6],
                        fontsize=8,
                        color="black",
                        alpha=0.7,
                    )
                    fnip[page][index] = unicode[count][2:6]
                index += 1
            count += 1

# def print_font(count, page, fnip):
#     index = 0
#     X = np.arange(7.5, 192.5, 20)
#     Y = np.arange(21, 281, 26)
#     for j in range(10):
#         for i in range(10):
#             if count >= 190:
#                 plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
#             else:
#                 try:
#                     if unicode[count] == "123" or count >= 190:
#                         plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
#                         fnip[page][index] = ""
#                     else:
#                         plt.text(
#                             X[i] + 1,
#                             Y[j] - 3,
#                             unicode[count].encode("ascii").decode("unicode-escape"),
#                             fontsize=14,
#                             color="black",
#                             alpha=0.7,
#                         )
#                         plt.text(
#                             X[i] + 8.5,
#                             Y[j] - 3,
#                             unicode[count][2:6],
#                             fontsize=8,
#                             color="black",
#                             alpha=0.7,
#                         )
#                         fnip[page][index] = unicode[count][2:6]
#                 except UnicodeDecodeError as e:
#                     # Handle the UnicodeDecodeError here (e.g., print a message, log it, or skip the entry).
#                     print(f"Error processing entry {count}: {str(e)}")
#                     plt.text(X[i], Y[j] - 2, "", fontsize=15, color="black", alpha=0.7)
#                     fnip[page][index] = ""  # You can decide what to do in case of an error.
#                 index += 1
#             count += 1

            
def table_square(axes):
    X = np.arange(7.5, 192.5, 20)
    Y = np.arange(21, 281, 26)
    for j in range(10):
        for i in range(10):
            rect = patches.Rectangle(
                (X[i], Y[j]),
                15,
                15,
                linewidth=1,
                #edgecolor="#9ACD32",
                edgecolor="#000000",
                alpha=1,
                #facecolor="black",
                facecolor="#3C3C3C",
                fill=False,
            )
            axes.add_patch(rect)

            # 書寫輔助虛線
            # axes.plot([X[i]+7.5, X[i]+7.5], [Y[j], Y[j]+15], linewidth=0.4, color='#9ACD32', alpha=0.6, linestyle='--', dashes=(8, 8))
            # axes.plot([X[i], X[i]+15], [Y[j]+7.5, Y[j]+7.5], linewidth=0.4, color='#9ACD32', alpha=0.6, linestyle='--', dashes=(8, 8))
            # axes.plot([X[i], X[i]+15], [Y[j]+12, Y[j]+12], linewidth=0.4, color='#9ACD32', alpha=0.6, linestyle='--', dashes=(8, 8))

            axes.plot(
                [X[i] + 0.5, X[i] + 2],
                [Y[j] - 7.5, Y[j] - 7.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )  ## v
            axes.plot(
                [X[i] + 5, X[i] + 6.5],
                [Y[j] - 7.5, Y[j] - 7.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 0.5, X[i] + 2],
                [Y[j] - 1.5, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 5, X[i] + 6.5],
                [Y[j] - 1.5, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 0.5, X[i] + 0.5],
                [Y[j] - 7.5, Y[j] - 6],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )  ## h
            axes.plot(
                [X[i] + 0.5, X[i] + 0.5],
                [Y[j] - 3, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 6.5, X[i] + 6.5],
                [Y[j] - 7.5, Y[j] - 6],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )
            axes.plot(
                [X[i] + 6.5, X[i] + 6.5],
                [Y[j] - 3, Y[j] - 1.5],
                linewidth=0.4,
                color="black",
                alpha=0.4,
            )

        axes.plot(
            [5, 205],
            [Y[j] + 16.5, Y[j] + 16.5],
            linewidth=0.3,
            color="black",
            alpha=0.4,
        )  ## vvvv


def output_svg(filename):
    plt.axis("off")  # 刪除座標軸
    plt.xlim(0, 210)
    plt.ylim(297, 0)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)  # 刪除白邊
    plt.margins(0, 0)
    plt.savefig("./Table/" + filename + ".svg")


def pipeline(args):
    (page, count) = args
    create_plot(page)
    print_font(count, page, fnip)
    output_svg("{:03d}".format(page + 1))
    plt.close(page)


fnip = [[""] * 100 for _ in range(info.TOTAL_PAGES)]  # Font Number in Page (Unicode)
unicode = read_json("./CP950.json")

if __name__ == "__main__":
    cpus = mp.cpu_count()  # count of CPU cores
    print(f"Using {cpus = }")
    pool = mp.Pool(cpus)
    args = zip(range(0, info.TOTAL_PAGES), range(0, info.TOTAL_PAGES * 100 + 1, 100))
    for _ in tqdm(pool.imap_unordered(pipeline, args), total=info.TOTAL_PAGES):
        ...
    pool.close()
    pool.join()