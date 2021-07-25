import os, csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

articles = list()
with open("article-ids.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for record in csv_reader:
        articles.append(record[1])

edges = list()
i = 1
with open('wikispeedia_paths-and-graph//shortest-path-distance-matrix.txt') as f:
    for line in f:
        if (line[0].isdigit() or line[0] == '_'):
            
            for l in range(len(line)):
                if line[l] == '1':
                    edges.append([articles[i], articles[l+1]])
            
            i+=1

edges.sort()
edges.insert(0, ['From_ArticleID', 'To_ArticleID'])
with open("edges.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(edges)

