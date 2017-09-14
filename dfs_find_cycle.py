#/usr/bin/env python
#encoding:utf-8

#Author Mi

graph = {}
graph['a'] = ['b','c']
graph['b'] = ['d']
graph['c'] = []
graph['d'] = ['e']
graph['e'] = ['a']

cv = {}
gv = {}
for key in graph.keys():
    cv[key] = False
    gv[key] = False
    
def dfs_c(graph, node, cv, gv):
    if gv[node]:
        return False
    cv[node] = True
    gv[node] = True
    for nei in graph[node]:
        if cv[nei] or dfs_c(graph, nei, cv, gv):
            return True
    cv[node] = False
    return False

for key in graph.keys():
    if dfs_c(graph, key, cv, gv):
        print "Yes"
        exit()
print "No"
