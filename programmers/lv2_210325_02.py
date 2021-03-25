'''
배달 - 그래프

문제 설명
N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 
각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다. 다음은 N = 5, K = 3인 경우의 예시입니다.
위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다. 그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다. 따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
-마을의 개수 N은 1 이상 50 이하의 자연수입니다.
-road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
-road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
-road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
-a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
-두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
-한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
-K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
-임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
-1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.
'''

from collections import deque


def solution(N, road, K):
    nodes = {}
    dist = {i : float('inf') if i != 1 else 0 for i in range(1, N+1)}
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    queue = deque([1])
    
    while queue:
        crnt_node = queue.popleft()
        for nxt_node, d in nodes[crnt_node]:
            if dist[nxt_node] > dist[crnt_node] + d:
                dist[nxt_node] = dist[crnt_node] + d
                queue.append(nxt_node)

    return len([dist for dist in dist.values() if dist <= K])

' ----- '

def solution(N, road, K):
    costs = [float('inf')] * (N + 1)
    costs[1] = 0
    parents = [1]          
    
    while (parents):
        parent = parents.pop(0)
        for a, b, cost in road:
            if (a == parent or b == parent):
                target = b if a == parent else a
                if costs[target] > costs[parent] + cost:
                    costs[target] = costs[parent] + cost
                    parents.append(target)

    return sum(1 for c in costs if c <= K)
