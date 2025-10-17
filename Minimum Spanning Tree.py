# Minimum Spanning Tree

V = 5
G = [
    [0, 4, 0, 5, 2],
    [4, 0, 1, 3, 0],
    [0, 1, 0, 8, 0],
    [5, 3, 8, 0, 2],
    [2, 0, 0, 2, 0]
]
sel = [0]*V
sel[0] = 1
e = 0
print("\nEdge : Weight\n")

while e < V-1:
    m, x, y = 9999, 0, 0
    for i in range(V):
        if sel[i]:
            for j in range(V):
                if not sel[j] and G[i][j]:
                    if G[i][j] < m:
                        m, x, y = G[i][j], i, j
    print(f"{x}-{y}: {G[x][y]}")
    sel[y] = 1
    e += 1
