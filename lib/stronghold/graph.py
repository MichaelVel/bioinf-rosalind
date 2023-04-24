from typing import Iterator, Self
from itertools import permutations

class Node:
    def __init__(self, name: str, dna: str) -> None:
        self.name = name
        self.dna = dna

    def overlapping(self, other: Self, k: int) -> bool:
        return self.suffix(k) == other.prefix(k)

    def prefix(self, k: int) -> str: return self.dna[:k]

    def suffix(self, k: int) -> str: return self.dna[-k:]

    def __str__(self) -> str:
        return self.name

class Edge:
    def __init__(self, fromNode: Node, toNode: Node) -> None:
        self.fromNode = fromNode
        self.toNode = toNode

    def __str__(self) -> str:
        return f"{self.fromNode} {self.toNode}"

class OverlapGraph:
    def __init__(self, nodes: list[Node], k: int) -> None:
        self.k: int = k
        self.a_list: list[Edge] = []
        #self._edges_from_nodes(nodes)
        self._edges_from_nodes_hashmap(nodes)

    def _edges_from_nodes(self, nodes: list[Node]) -> None:
        for head, tail in permutations(nodes, 2):
            if head.overlapping(tail, self.k):
                self.a_list.append(Edge(head,tail))

    def _edges_from_nodes_hashmap(self, nodes: list[Node]) -> None:
        map = {node.suffix(self.k): node for node in nodes}
        for node in nodes:
            suff = node.prefix(self.k)
            if suff in map and node != (head := map[suff]):
                self.a_list.append(Edge(head,node))

    def adjacency_list(self) -> Iterator[Edge]:
        return iter(self.a_list)


def main(input: str) -> str:
    node_list: list[Node] = []

    for segment in input.split(">")[1:]:
        dna = [l for l in segment.splitlines() if "Rosalind" not in l]
        name = segment.split()[0]
        node_list.append(Node(name,''.join(dna)))

    graph = OverlapGraph(node_list, 3)
    return '\n'.join(str(edge) for edge in graph.adjacency_list())

if __name__ == "__main__":
    TEST_INPUT = ("""\
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
""")
    print(main(TEST_INPUT))


    

    
