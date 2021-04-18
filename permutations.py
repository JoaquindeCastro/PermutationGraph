for n in nodes:
    rem = [x for x in nodes if x!=n]
    for m in rem:
        if list(n.name)[0] == list(m.name)[0] or list(n.name)[2] == list(m.name)[2]:
           if m not in g.childrenOf(n):
               g.addEdge(Edge(n,m))
