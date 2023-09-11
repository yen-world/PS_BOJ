def preorder(root):
    global result
    result += root
    if graph[root][0] != ".":
        preorder(graph[root][0])
    if graph[root][1] != ".":
        preorder(graph[root][1])
    return result


def inorder(root):
    global result
    if graph[root][0] != ".":
        inorder(graph[root][0])
    result += root
    if graph[root][1] != ".":
        inorder(graph[root][1])
    return result


def postorder(root):
    global result
    if graph[root][0] != ".":
        postorder(graph[root][0])
    if graph[root][1] != ".":
        postorder(graph[root][1])
    result += root
    return result


n = int(input())
graph = {}

for i in range(n):
    root_node, left_node, right_node = input().split()
    if graph.get(root_node) == None:
        graph[root_node] = []
    graph[root_node].append(left_node)
    graph[root_node].append(right_node)

result = ""
print(preorder("A"))

result = ""
print(inorder("A"))

result = ""
print(postorder("A"))
