import math
import sys
class Graph():
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)]
                    for row in range(dinh)]

    def inketqua(cung, L, a):
        print ("đỉnh nguồn xuất phát từ: ")
        for nut in range(cung.x):
            print (a," đến đỉnh ",nut, "độ dài đường đi là: ", L[nut])
    def duongdinhonhat(cung, L, P):
        min = sys.maxsize
        for x in range(cung.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x
        return min_index
    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0
        P = [False] * cung.x
        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            P[u] = True
            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False and L[x] > L[u]+ cung.graph[u][x]:
                    L[x] = L[u] + cung.graph[u][x]
    
            cung.inketqua(L, a)



print('đồ thị vô hướng')
g = Graph(6)
g.graph = [[0, 2, 0, 3, 0, 0],

        [2, 0, 7, 2, 1, 0],
        [0, 7, 0, 0, 0, 3],
        [3, 2, 0, 0, 2, 0],
        [0, 1, 0, 2, 0, 4],
        [0, 0, 3, 0, 4, 0]
    ];
g.timduongdi(0);

print('Đồ thị có hướng')
g = Graph(6)
g.graph = [[0, 3, 0, 1, 0, 0],

        [0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 3],
        [0, 0, 9, 0, 2, 0],
        [0, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 0]
    ];
g.timduongdi(0);






