# Ch4 - Q1. Find Routes between Nodes
from Queue import Queue


def dfs(start, find, adj_list):
    if start not in adj_list:
        return False

    if find in adj_list[start]:
        return True

    for node in adj_list[start]:
        if dfs(node, find, adj_list):
            return True

    return False


def bfs(start, find, adj_list):
    queue = Queue()
    queue.enqueue(start)
    isFound = False

    while not queue.isEmpty():
        check = queue.dequeue()

        if check not in adj_list:
            continue

        if find in adj_list[check]:
            isFound = True
            break

        for node in adj_list[check]:
            queue.enqueue(node)

    return isFound


def make_graph(arr):
    adj_list = {}

    for nodes in arr:
        if nodes[0] in adj_list:
            adj_list[nodes[0]].append(nodes[1])
        else:
            adj_list[nodes[0]] = [nodes[1]]

    return adj_list


def find_route_dfs(nodes, adj_list):
    return dfs(nodes[0], nodes[1], adj_list) or dfs(nodes[1], nodes[0], adj_list)


def find_route_bfs(nodes, adj_list):
    return bfs(nodes[0], nodes[1], adj_list) or bfs(nodes[1], nodes[0], adj_list)


nodes = [[0, 2], [2, 3], [0, 1]]

graph = make_graph(nodes)

print('find route DFS:')
print('Route 0 -> 3', find_route_dfs([0, 3], graph))
print('Route 2 -> 1', find_route_dfs([2, 1], graph))
print('Route 1 -> 3', find_route_dfs([1, 3], graph))
print()
print('find route BFS:')
print('Route 0 -> 3', find_route_bfs([0, 3], graph))
print('Route 2 -> 1', find_route_bfs([2, 1], graph))
print('Route 1 -> 3', find_route_bfs([1, 3], graph))
