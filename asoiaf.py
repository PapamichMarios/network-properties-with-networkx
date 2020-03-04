import networkx as nx
import pandas as pd
import degree_distribution
 
# read all the 5 csv files
# keep only the distinct pairs of source target since we will ignore the books and the weights
 
all_books = ["book1.csv", "book2.csv", "book3.csv", "book4.csv", "book5.csv"]
 
li = []
 
for f in all_books:
    tmp = pd.read_csv(f)
    li.append(tmp)
 
df = pd.concat(li, axis=0, ignore_index=True)
 
df = df[['Source', 'Target']]
df.drop_duplicates(subset=['Source', 'Target'], inplace=True)

#print(df.head(20))
 
# create the ASOIAF networkx object
G = nx.from_pandas_edgelist(df,  source='Source', target='Target')

# create a random graph networkx object
#G = nx.erdos_renyi_graph(len(G.nodes()), 2*len(G.edges())/(len(G.nodes())*(len(G.nodes())-1)))
#G = nx.watts_strogatz_graph(len(G.nodes()), 7, 0.3)

print("\n\nNumber of nodes: %d" % len(G.nodes()))
 
print("\n\nNumber of edges: %d" % len(G.edges()))

graphs = list(nx.connected_component_subgraphs(G))
print("\n\nConnected components: %d (size: %d)" % (len(graphs), len(graphs[0].nodes())))

print("\n\nAverage shortest path: %f" % nx.average_shortest_path_length(graphs[0]))

print("\n\nDiameter: %d" % nx.diameter(graphs[0]))

print("\n\nAverage clustering coefficient: %f" % nx.average_clustering(G))

degree_distribution.plot_degree_distribution(graphs[0])

