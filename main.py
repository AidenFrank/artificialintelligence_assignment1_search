# This code is the property of Aiden Frank

# We use deque for some queue operations
from collections import deque
# We import time to check the speed of the algorithms
import time
# We import random to compare the algorithms
import random
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

# We list the sld heuristic for any other city to Bucharest to be used with the Best First (greedy algorithm) and A* Algorithm
sld_heuristic = {
    1: 366, 2: 0, 3: 160, 4: 242, 5: 161, 6: 176, 7: 77, 8: 151, 9: 226, 10: 244, 11: 241, 12: 234, 13: 380, 14: 100, 15: 193, 16: 253, 17: 329, 18: 80, 19: 199, 20: 374
}

# 1 Breadth First Search
def BFS(start, goal):
    # We start time here and then whenever the function returns, we grab the ending time and return the time of execution for analysis
    start_time = time.time()
    # If our start or goal city doesn't exist, then there is not path so we return an empty list
    if start not in cities_adjacency_list or goal not in cities_adjacency_list:
        # We get the ending time
        end = time.time()
        # We return the resulting path, the number of visited cities, and the time of execution
        return [], 0, end - start_time
    # Keep track of the visited cities
    visited = []
    # Create our queue and begin at start city
    # Also add our start city to the visited cities
    queue = deque([(start, [start])])
    # Loop until we reach the goal or come up with nothing
    while queue:
        # Get the current city and also add it to the path
        cur_city, path = queue.popleft()
        # If the current city is our goal, then we are done and can return path
        if cur_city == goal:
            # We get the ending time
            end = time.time()
            # We return the resulting path, the number of visited cities, and the time of execution
            return path, len(visited), end - start_time
        # If the current city is not our path, then we need to say we've visited this city and then look around at adjacent cities in a breadth first search
        visited.append(cur_city)
        # Go through all the adjacent cities and if they aren't visited, add them all to the end of the list
        for adj_city in cities_adjacency_list.get(cur_city, []):
            # Get the id of the adjacent city
            adj_city_id = adj_city[0]
            # Check if it has been visited yet, if not, add it to the queue
            if adj_city_id not in visited:
                queue.append((adj_city_id, path + [adj_city_id]))
                visited.append(adj_city_id)
            # Now that the adjacent cities are added to the end of the queue, the loop will repeat and check these cities for the goal city
    # If somehow we couldn't reach the goal city and the queue became empty, there is no path so we return an empty list
    # We get the ending time
    end = time.time()
    # We return the resulting path, the size of it, and the time of execution
    return [], len(visited), end - start_time

# 2 Depth First Search
def DFS(start, goal):
    # We start time here and then whenever the function returns, we grab the ending time and return the time of execution for analysis
    start_time = time.time()
    # If our start or goal city doesn't exist, then there is not path so we return an empty list
    if start not in cities_adjacency_list or goal not in cities_adjacency_list:
        # We get the ending time
        end = time.time()
        # We return the resulting path, the number of visited cities, and the time of execution
        return [], 0, end - start_time
    # Keep track of the visited cities
    visited = []
    # Create our queue and begin at start city
    # Also add our start city to the visited cities
    queue = deque([(start, [start])])
    # Loop until we reach the goal or come up with nothing
    while queue:
        # Get the current city and also add it to the path
        cur_city, path = queue.popleft()
        if cur_city == goal:
            # We get the ending time
            end = time.time()
            # We return the resulting path, the number of visited cities, and the time of execution
            return path, len(visited), end - start_time
        # If the current city is not our path, then we need to say we've visited this city and then look around at adjacent cities in a depth first search
        visited.append(cur_city)
        # Go through all the adjacent cities and if they aren't visited, add them in reverse order to ensure the first adjacent city is at the front of the queue
        for adj_city in reversed(cities_adjacency_list.get(cur_city, [])):
            # Get the id of the adjacent city
            adj_city_id = adj_city[0]
            # Check if it has been visited yet, if not, add it to the queue
            if adj_city_id not in visited:
                # Notice that we appendleft, instead of just append like in BFS
                queue.appendleft((adj_city_id, path + [adj_city_id]))
                visited.append(adj_city_id)
            # Now that the cities are added to the front of the queue, the loop will repeat and check the first child of the current node first
    # If somehow we couldn't reach the goal city and the queue became empty, there is no path so we return an empty list
    # We get the ending time
    end = time.time()
    # We return the resulting path, the size of it, and the time of execution
    return [], len(visited), end - start_time

# 3 Best First (greedy algorithm) Note: we use the data from the text book for the SLD from every other city to Bucharest, so only the starting city is a parameter here, the goal is always Bucharest
def BF(start):
    # We start time here and then whenever the function returns, we grab the ending time and return the time of execution for analysis
    start_time = time.time()
    # If our start city doesn't exist, then there is not path so we return an empty list
    if start not in cities_adjacency_list:
        # We get the ending time
        end = time.time()
        # We return the resulting path, the number of visited cities, and the time of execution
        return [], 0, end - start_time
    # Keep track of the visited cities
    visited = []
    # Create our queue and begin at start city
    # Also add our start city to the visited cities
    queue = deque([(start, [start])])
    # Loop until we reach the Bucharest or come up with nothing
    while queue:
        # Get the current city and also add it to the path
        cur_city, path = queue.popleft()
        # If the current city is Bucharest, then we are done and can return path
        if cur_city == 2:
            # We get the ending time
            end = time.time()
            # We return the resulting path, the number of visited cities, and the time of execution
            return path, len(visited), end - start_time
        # If the current city is not in our path, then we need to say we've visited this city and then look around at adjacent cities and thier SLDs
        visited.append(cur_city)
        # Go through all the adjacent cities and if they aren't visited, add them to a list to compare their SLDs
        adjacent_cities = []
        for adj_city in cities_adjacency_list.get(cur_city, []):
            # Get the id of the adjacent city
            adj_city_id = adj_city[0]
            # Check if it has been visited yet, if not, add it to the list of adjacent cities
            if adj_city_id not in visited:
                adjacent_cities.append((adj_city_id, path + [adj_city_id]))
        # Now sort the adjacent cities by their ID and add them to the queue based on their SLD
        adjacent_cities.sort(key=lambda x: sld_heuristic.get(x[0], float('inf')))
        for city in adjacent_cities:
            queue.append(city)
        # Now that the cities are added to the queue based on their SLD, we can continue to loop through the queue and find the next SLD
    # If somehow we couldn't reach the goal city and the queue became empty, there is no path so we return an empty list
    # We get the ending time
    end = time.time()
    # We return the resulting path, the size of it, and the time of execution
    return [], len(visited), end - start_time

# 4 A* Algorithm Note: we use the data from the text book for the SLD from every other city to Bucharest, so only the starting city is a parameter here, the goal is always Bucharest
def A(start):
    # We start time here and then whenever the function returns, we grab the ending time and return the time of execution for analysis
    start_time = time.time()
    # If our start city doesn't exist, then there is not path so we return an empty list
    if start not in cities_adjacency_list:
        # We get the ending time
        end = time.time()
        # We return the resulting path, the number of visited cities, and the time of execution
        return [], 0, end - start_time
    # Keep track of the visited cities
    visited = []
    # Create our queue and begin at start city
    # Also add our start city to the visited cities and its g(n) cost to reach the node
    queue = deque([(start, [start], 0)])
    # Loop until we reach the Bucharest or come up with nothing
    while queue:
        # Firstly we sort the queue by f(n), the estimated cost of the cheapest solution through n
        # What we're doing here is getting the sld_heuristic from the list based on what city we're looking at
        # then adding it to the g(n) cost from start to the city to get the f(n) for each city in the queue, then finally sorting them from lowest to highest f(n)
        queue = deque(sorted(queue, key=lambda x: x[2] + sld_heuristic.get(x[0], float('inf'))))
        # Now that the queue has been sorted by lowest to highest f(n), get the city with the lowest f(n)
        # Also get the g(n) of it
        cur_city, path, g_n = queue.popleft()
        # If the current city is Bucharest, then we are done and can return path
        if cur_city == 2:
            # We get the ending time
            end = time.time()
            # We return the resulting path, the number of visited cities, and the time of execution
            return path, len(visited), end - start_time
        # If the current city is not in our path, then we need to say we've visited this city and then look around at adjacent cities and thier SLDs
        visited.append(cur_city)
        # Look through all the adjacent cities and appened them to our queue
        for adj_city, cost in cities_adjacency_list.get(cur_city, []):
            # Check if it has been visited yet, if not then add it to our queue
            if adj_city not in visited:
                # Get the adjacent city's g_n cost so far
                g_new = g_n + cost
                # Append to the queue
                queue.append((adj_city, path + [adj_city], g_new))
        # Now that the cities are added to the queue, they will be re-sorted based on f(n) and a new node to travel to will be picked
    # If somehow we couldn't reach the goal city and the queue became empty, there is no path so we return an empty list
    # We get the ending time
    end = time.time()
    # We return the resulting path, the size of it, and the time of execution
    return [], len(visited), end - start_time

# This function runs all of the algorithms we've implemented 100 times and compares their correctness and efficiency
def algorithm_comparison():

    # We test all of the algorithms with the same start and goal values and compare their results
    # Set up BFS comparison variables
    BFS_correctness = 0
    BFS_average_visited = 0
    BFS_average_time = 0
    # Set up DFS comparison variables
    DFS_correctness = 0
    DFS_average_visited = 0
    DFS_average_time = 0
    # Set up Best First (greedy algorithm) variables
    BF_correctness = 0
    BF_average_visited = 0
    BF_average_time = 0
    # Set up the A* algorithm variables
    A_correctness = 0
    A_average_visited = 0
    A_average_time = 0
    for i in range(100):
        # Get a random start and set the goal to Bucharest
        rand_start = random.randint(1, 20)
        goal = 2
        # Run BFS and store result in a variable
        resultuple = BFS(rand_start, goal)
        # Check for correctness, if correct add one to the correctness score (also check to make sure the resulting path isn't 0)
        if len(resultuple[0]) != 0 and resultuple[0][0] == rand_start and resultuple[0][len(resultuple[0]) - 1] == goal:
            BFS_correctness += 1
        # Add the number of visited cities to the average, divided by 100 later
        BFS_average_visited += resultuple[1]
        # Add the time to execute to the average time, divided by 100 later
        BFS_average_time += resultuple[2]
        # Run DFS and store result in a variable
        resultuple = DFS(rand_start, goal)
        # Check for correctness, if correct add one to the correctness score (also check to make sure the resulting path isn't 0)
        if len(resultuple[0]) != 0 and resultuple[0][0] == rand_start and resultuple[0][len(resultuple[0]) - 1] == goal:
            DFS_correctness += 1
        # Add the number of visited cities to the average, divided by 100 later
        DFS_average_visited += resultuple[1]
        # Add the time to execute to the average time, divided by 100 later
        DFS_average_time += resultuple[2]
        # Run Best First (greedy algorithm) and store result in a variable
        resultuple = BF(rand_start)
        # Check for correctness, if correct add one to the correctness score (also check to make sure the resulting path isn't 0)
        if len(resultuple[0]) != 0 and resultuple[0][0] == rand_start and resultuple[0][len(resultuple[0]) - 1] == goal:
            BF_correctness += 1
        # Add the number of visited cities to the average, divided by 100 later
        BF_average_visited += resultuple[1]
        # Add the time to execute to the average time, divided by 100 later
        BF_average_time += resultuple[2]
        # Run A* and store result in a variable
        resultuple = A(rand_start)
        # Check for correctness, if correct add one to the correctness score (also check to make sure the resulting path isn't 0)
        if len(resultuple[0]) != 0 and resultuple[0][0] == rand_start and resultuple[0][len(resultuple[0]) - 1] == goal:
            A_correctness += 1
        # Add the number of visited cities to the average, divided by 100 later
        A_average_visited += resultuple[1]
        # Add the time to execute to the average time, divided by 100 later
        A_average_time += resultuple[2]
    # Get the BFS averages
    BFS_average_visited = BFS_average_visited / 100.0
    BFS_average_time = BFS_average_time / 100.0
    # Get the DFS averages
    DFS_average_visited = DFS_average_visited / 100.0
    DFS_average_time = DFS_average_time / 100.0
    # Get the BF averages
    BF_average_visited = BF_average_visited / 100.0
    BF_average_time = BF_average_time / 100.0
    # Get the A averages
    A_average_visited = A_average_visited / 100.0
    A_average_time = A_average_time / 100.0
    # Print the results for all
    print(f"BFS earned a corectness score of {BFS_correctness}/100")
    print(f"The average number of cities BFS visited in its tests was {BFS_average_visited}")
    print(f"The average time BFS took to finish its tests was {BFS_average_time} seconds")
    # Algorithm result splitter
    print("--------")
    print(f"DFS earned a corectness score of {DFS_correctness}/100")
    print(f"The average number of cities DFS visited in its tests was {DFS_average_visited}")
    print(f"The average time DFS took to finish its tests was {DFS_average_time} seconds")
    print("--------")
    print(f"BF earned a corectness score of {BF_correctness}/100")
    print(f"The average number of cities BF visited in its tests was {BF_average_visited}")
    print(f"The average time BF took to finish its tests was {BF_average_time} seconds")
    print("--------")
    print(f"A* earned a corectness score of {A_correctness}/100")
    print(f"The average number of cities A* visited in its tests was {A_average_visited}")
    print(f"The average time A* took to finish its tests was {A_average_time} seconds")

# This calls the comparion function
algorithm_comparison()