from collections import defaultdict
class Graph:
    def __init__(self):
        self.out_neighbour = defaultdict(list)
    def add_edge(self, from_node, to_node):
        self.out_neighbour[from_node].append(to_node)
        self.out_neighbour[to_node].append(from_node)
    def second_order_rank(self, from_node):
        first_order_set = set()
        for n in self.out_neighbour[from_node]:
            first_order_set.add(n)
        second_order_rank = defaultdict(int) # key: node id, value: count of common first order connection
        for first_order_node in self.out_neighbour[from_node]:
            for second_order_node in self.out_neighbour[first_order_node]:
                if second_order_node == from_node or second_order_node in first_order_set:
                    continue
                for second_order_neighbour in self.out_neighbour[second_order_node]:
                    if second_order_neighbour in first_order_set:
                        second_order_rank[second_order_node] += 1
        rank_order = []
        for n,c in second_order_rank.items():
            rank_order.append((c,n))
        rank_order = sorted(rank_order, reverse=True)
        result = []
        for r in rank_order:
            result.append(r[1])
        return result
if __name__ == "__main__":
    g = Graph()
    edges = [(1,2),(1,3),(2,3),(2,4),(2,5),(3,4),(3,6),(4,7),(4,10),(5,9),(6,8)]
    for e in edges:
        g.add_edge(e[0],e[1])
    print(g.second_order_rank(1))