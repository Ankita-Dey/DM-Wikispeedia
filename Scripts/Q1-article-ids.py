import csv, os
from math import log10, ceil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filepath = 'wikispeedia_paths-and-graph//articles.tsv'

with open(filepath, 'r') as f:
    articles = list(csv.reader(f))

articles = articles[12:]

output=list()
count = 1
for article in articles:
    id = 'A' + '0'*(4-ceil(log10(count+1))) + str(count)
    output.append([article[0], id])
    count+=1

output.sort()
output.insert(0, ['Article_Name', 'Article_ID'])

with open("article-ids.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)
