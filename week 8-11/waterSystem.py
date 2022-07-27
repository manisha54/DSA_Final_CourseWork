# from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import json

G = nx.DiGraph()


def addNewHouse(house_num, update=True):
    G.add_node(house_num)
    if update:
        appData["nodes"].append(house_num)
        with open(r"week 8-11/appData.json", "w") as jsonFile:
            json.dump(appData, jsonFile)


def addPipeConnection(house1, house2, update=True):
    G.add_edge(house1, house2, weight=1)
    if checkCycle():
        G.remove_edge(house1, house2)
        return False
    if update:
        appData["edges"].append([house1, house2])
        with open(r"week 8-11/appData.json", "w") as jsonFile:
            json.dump(appData, jsonFile)
    return True


def displayPipeSystem(plotShortestPath=False, src=0, dest=0):
    # plt.figure(figsize=(7, 7))
    print(f"Houses : {G.nodes}")
    plt.clf()
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="teal")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.4)

    if plotShortestPath:
        path = nx.shortest_path(G, source=src, target=dest)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               edge_color='r', width=5)

    plt.show()


def checkCycle():
    try:
        nx.find_cycle(G, orientation="original")
        return True
    except:
        return False


def reset():
    with open(r"week 8-11/appData.json", "w") as jsonFile:
        json.dump({"nodes": [], "edges": []}, jsonFile)


f = open(r"week 8-11/appData.json")
appData = json.load(f)

for node in appData["nodes"]:
    addNewHouse(node, update=False)

for edge in appData["edges"]:
    addPipeConnection(edge[0], edge[1], update=False)
f.close()
