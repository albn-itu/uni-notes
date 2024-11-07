import itertools
from typing import final, override

EMPTYSET = "\\emptyset"


class Node:
    value: set[str] = set()

    @staticmethod
    def get_value_as_set_string(values: set[str]) -> str:
        if not values:
            return EMPTYSET
        return "\\{" + ", ".join(sorted(list(values))) + "\\}"

    @staticmethod
    def print_dp(first: str, second: str, result: str):
        print(f"DP[{first}][{second}] &= {result} = \\\\")

    @staticmethod
    def get_combs_of_set(values: set[str]) -> list[set[str]]:
        combs: list[set[str]] = []
        for i in range(len(values) + 1):
            combs.extend(map(set, itertools.combinations(values, i)))
        return combs

    def get_combs(self) -> list[set[str]]:
        return Node.get_combs_of_set(self.value)

    def create_relations(self):
        pass


class Leaf(Node):
    @override
    def create_relations(self):
        print("\\intertext{Leaf}")
        Node.print_dp(EMPTYSET, EMPTYSET, "0")


@final
class Introduce(Node):
    new: str
    child: Node

    def __init__(self, new: str, child: Node):
        self.value = child.value.copy()
        self.value.add(new)
        self.new = new
        self.child = child

    @override
    def create_relations(self):
        print(f"\\intertext{{Introduce {self.new}}}")

        child_str = self.get_value_as_set_string(self.child.value)

        relations: list[tuple[str, str]] = []
        relations.append((EMPTYSET, f"DP[{child_str}][{EMPTYSET}] + 1"))
        relations.append((self.new, f"DP[{child_str}][{EMPTYSET}]"))

        for value in self.value:
            if value != self.new:
                relations.append((value, f"DP[{child_str}][{value}] + 1"))

        self_str = self.get_value_as_set_string(self.value)
        for relation in relations:
            Node.print_dp(self_str, relation[0], relation[1])


@final
class Forget(Node):
    forget: str
    child: Node

    def __init__(self, forget: str, child: Node):
        self.value = child.value.copy()
        self.value.remove(forget)
        self.forget = forget
        self.child = child

    @override
    def create_relations(self):
        print(f"\\intertext{{Forget {self.forget}}}")
        child_str = self.get_value_as_set_string(self.child.value)

        relations: list[tuple[str, str]] = []
        relations.append(
            (
                EMPTYSET,
                f"min(DP[{child_str}][{EMPTYSET}], DP[{child_str}][{self.forget}])",
            )
        )
        for value in self.value:
            relations.append((value, f"DP[{child_str}][{value}]"))

        self_str = self.get_value_as_set_string(self.value)
        for relation in relations:
            Node.print_dp(self_str, relation[0], relation[1])


@final
class Join(Node):
    left: Node
    right: Node

    def __init__(self, left: Node, right: Node):
        self.value = left.value.union(right.value)
        self.left = left
        self.right = right

    @override
    def create_relations(self):
        print("\\intertext{Join}")
        left_str = self.get_value_as_set_string(self.left.value)
        right_str = self.get_value_as_set_string(self.right.value)
        self_str = self.get_value_as_set_string(self.value)

        relations: list[tuple[str, str]] = []
        relations.append(
            (
                EMPTYSET,
                f"DP[{left_str}][{EMPTYSET}] + DP[{right_str}][{EMPTYSET}] - |{self_str}|",
            )
        )

        for value in self.value:
            relations.append(
                (
                    value,
                    f"DP[{left_str}][{value}] + DP[{right_str}][{value}] - (|{self_str}| - 1)",
                )
            )

        for relation in relations:
            Node.print_dp(self_str, relation[0], relation[1])


if __name__ == "__main__":
    nodes: list[Node] = []
    nodes.append(Leaf())
    nodes.append(Introduce("e", nodes[0]))
    nodes.append(Introduce("g", nodes[1]))
    nodes.append(Introduce("f", nodes[2]))
    nodes.append(Forget("f", nodes[3]))
    nodes.append(Introduce("b", nodes[4]))

    nodes.append(Leaf())
    nodes.append(Introduce("b", nodes[6]))
    nodes.append(Introduce("h", nodes[7]))
    nodes.append(Introduce("g", nodes[8]))
    nodes.append(Forget("h", nodes[9]))
    nodes.append(Introduce("e", nodes[10]))

    nodes.append(Join(nodes[5], nodes[11]))

    for node in nodes:
        node.create_relations()
