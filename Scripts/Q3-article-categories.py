import pandas as pd
import csv, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv('article-ids.csv')
articleid = df.set_index(['Article_Name']).to_dict(orient='dict')['Article_ID']

df = pd.read_csv('category-ids.csv')
categoryid = df.set_index(['Category_Name']).to_dict(orient='dict')['Category_Id']

filepath = 'wikispeedia_paths-and-graph//categories.tsv'

with open(filepath, 'r') as f:
    articlecatlist = list(csv.reader(f, delimiter = '\t'))

articlecatlist = articlecatlist[13:]

articlecat = dict()
for i in range(len(articlecatlist)):
    if articleid[articlecatlist[i][0]] in articlecat:
        articlecat[articleid[articlecatlist[i][0]]].append(articlecatlist[i][1])
        
    else:
        articlecat[articleid[articlecatlist[i][0]]] = [articlecatlist[i][1]]

output = []

articles = list(articleid.values())
articles.sort()

for article in articles:
    if article not in articlecat:
        output.append([article, 'C0001'])
    
    else:
        catid = set()
        for category in articlecat[article]:
            catid.add(categoryid[category])

        catid = list(catid)
        catid.sort()
        output.append([article, ','.join(catid)])

output.sort()
output.insert(0, ['Article_ID', 'Category_ID'])

with open("article-categories.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)
