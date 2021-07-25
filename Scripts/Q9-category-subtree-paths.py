import csv, os
import networkx as nx
import pandas as pd


os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('edges.csv', 'r') as f:
    edges = list(csv.reader(f))

G = nx.DiGraph()
G.add_edges_from(edges[1:])


df = pd.read_csv('article-ids.csv')
articleid = df.set_index(['Article_Name']).to_dict(orient='dict')['Article_ID']

df = pd.read_csv('category-ids.csv')
categoryid = df.set_index(['Category_Name']).to_dict(orient='dict')['Category_Id']
idcategory = df.set_index(['Category_Id']).to_dict(orient='dict')['Category_Name']
categories = list(categoryid.values())
categories.sort()

df = pd.read_csv('article-categories.csv')
articlecat = df.set_index(['Article_ID']).to_dict(orient='dict')['Category_ID']



filepath = 'wikispeedia_paths-and-graph//paths_finished.tsv'

with open(filepath, 'r') as f:
    csv_reader = list(csv.reader(f, delimiter = '\t'))

csv_reader = csv_reader[16:]

humanpaths = list()     # human path, path length without back

for row in csv_reader:
    tmp = row[3].split(';')
    if len(tmp) > 1:
        
        if '<' in tmp:
            i = 0
            while(i<len(tmp)-1):
                if tmp[i+1] == '<':
                    tmp.pop(i)
                    tmp.pop(i)
                    if tmp[i] == '<':
                        i-=1
                else:
                    i+=1
        
        humanpaths.append(tmp)



hcatpath = dict()
hcattimes = dict()
scatpath = dict()
scattimes = dict()


for category in categories:
    hcatpath[category] = 0
    hcattimes[category] = 0
    scatpath[category] = 0
    scattimes[category] = 0


def addparents(cats):
    parents = list()

    # if 'C0001' not in cats:
    #     parents.append('C0001')

    for category in cats:
        tmp = idcategory[category]
        # tmp = tmp[:tmp.rfind('.')]
        
        while(tmp.count('.') >= 1):
            tmp = tmp[:tmp.rfind('.')]
            parents.append(categoryid[tmp])
    
    cats.extend(parents)
    return list(set(cats))


for humanpath in humanpaths:
    categories.clear()
    
    try:
        shortestpath = nx.shortest_path(G, articleid[humanpath[0]], articleid[humanpath[-1]], None, 'dijkstra')
    except:
        # print(humanpath)
        continue

    for article in humanpath:
        cats = articlecat[articleid[article]].split(',')
        cats = addparents(cats)     # added
        categories.extend(cats)

    for category in categories:
        hcattimes[category]+=1
    for category in list(set(categories)):
        hcatpath[category]+=1
    
    
    
    categories.clear()
    for article in shortestpath:
        cats = articlecat[article].split(',')
        cats = addparents(cats)     # added
        categories.extend(cats)
        
    for category in categories:
        scattimes[category]+=1
    for category in list(set(categories)):
        scatpath[category]+=1
    
output = list()
categories = list(scatpath.keys())
categories.sort()

for category in categories:
    output.append([category, hcatpath[category], hcattimes[category], scatpath[category], scattimes[category]])

output.sort()
output.insert(0, ['Category_ID','Number_of_human_paths_traversed','Number_of_human_times_traversed','Number_of_shortest_paths_traversed','Number_of_shortest_times_traversed'])

with open("category-subtree-paths.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)

