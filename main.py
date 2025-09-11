# We create an adjacency list to hold all of the data about the cities we are traversing

# Arad 1 
# Bucharest 2
# Craiova 3
# Drobeta 4
# Eforie 5
# Fagaras 6
# Giurgiu 7
# Hirsova 8
# Iasi 9
# Lugoj 10
# Mehadia 11
# Neamt 12
# Oradea 13
# Pitesti 14
# Rimnicu Vilcea 15
# Sibiu 16
# Timisoara 17
# Urziceni 18
# Vaslui 19
# Zerind 20

# The key is the city, then the city has a list of edges with each edge being a different city's number and the distance to that city
cities_adjacency_list = {
    1: [[20, 75], [16, 140], [17, 118]],
    2: [[14, 101], [6, 211], [18, 85], [7, 90]],
    3: [[4, 120], [15, 146], [14, 138]],
    4: [[11, 75], [3, 120]],
    5: [[8, 86]],
    6: [[16, 99], [2, 211]],
    7: [[2, 90]],
    8: [[18, 98], [5, 86]],
    9: [[12, 87], [19, 92]],
    10: [[17, 111], [11, 70]],
    11: [[10, 70], [4, 75]],
    12: [[9, 87]],
    13: [[16, 151], [20, 71]],
    14: [[15, 97], [2, 101], [3, 138]],
    15: [[16, 80], [14, 97], [3, 146]],
    16: [[1, 140], [13, 151], [6, 99], [15, 80]],
    17: [[1, 118], [10, 111]],
    18: [[19, 142], [8, 98], [2, 85]],
    19: [[9, 92], [18, 142]],
    20: [[13, 71], [1, 75]]
}

# 1 Breadth First Search

