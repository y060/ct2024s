from tqdm import tqdm
from pikepdf import Pdf

import info

pdfs = [
    Pdf.open(f"./PDF/{i:03d}.svg.pdf") for i in tqdm(range(1, info.TOTAL_PAGES + 1))
]

# for i in tqdm(range(1, info.TOTAL_PAGES + 1)):
#     pdfs.append(Pdf.open(f"./PDF/{i:03d}.svg.pdf"))

output = Pdf.new()

for each in tqdm(pdfs):
    output.pages.extend(each.pages)

output.save(f"{info.ID}_{info.NAME}.pdf")
