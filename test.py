import networkx as nx
import matplotlib.pyplot as plt

#Takes input and creates the graph
def Create(G):
	v = input()
	adj = []
	#input the adjacency list and add to graph
	for i in range(v):
		temp = map(int,raw_input().split())
		adj.append(temp)
	G.add_nodes_from(range(v))
	for i in range(v-1):
		for j in range(i+1,v):
			if adj[i][j]>0:
				G.add_edge(i,j,{'weight':adj[i][j]})

#Takes the final graph and draws it.
def Draw(G):
	#create labels
	n = len(G.nodes())
	colors = []
	for i in range(n):
		if len(G.edges(i)) > 0:
			colors.append("#2faced")
		else:
			colors.append("#1ffdc4")
	pos = nx.spring_layout(G)
	temp = nx.get_edge_attributes(G,'weight')
	wts = []
	for i in G.edges():
		wts.append(temp[i])
	nx.draw_networkx(G,pos,node_size=1000,node_color=colors,width=5.0,edge_color=wts,edge_cmap=plt.cm.Reds,edge_vmin=0.1,edge_vmax=max(wts),font_size=16)
	labels = dict([((u,v),d['weight']) for u,v,d in G.edges(data=True)])
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,label_pos=0.35,font_size=16)
	plt.axis("off")
	plt.show()

#DFS
def DFS(G,O):
	source = input()
	O.add_nodes_from(G.nodes())
	O.add_edges_from(list(nx.dfs_edges(G,source)))
	temp = nx.get_edge_attributes(G,'weight') 
	attrs = {(u,v):temp[(u,v)] for (u,v) in O.edges()}
	#print attrs
	#print O.edges()
	nx.set_edge_attributes(O,'weight',attrs)
	
#main function
if __name__== "__main__":
	#define the graph structure
	G = nx.Graph()
	Create(G)
	O = nx.Graph()
	DFS(G,O)
	#print list(nx.dfs_edges(G,1))
	Draw(O)