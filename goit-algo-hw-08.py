import heapq


def min_cost_to_connect_all_cables(cables):
    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:

        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)

        cost = cable_1 + cable_2
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6]
print(min_cost_to_connect_all_cables(cables))
