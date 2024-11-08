import itertools
from typing import final, override
from collections import defaultdict

EMPTYSET = "\\emptyset"


class Node:
    value: set[str]
    dp: dict[str, dict[str, int]]

    def __init__(self):
        self.value = set()
        self.dp = defaultdict(lambda: {})

    @staticmethod
    def get_value_as_set_string(values: set[str]) -> str:
        if not values:
            return EMPTYSET
        return "\\{" + ", ".join(sorted(list(values))) + "\\}"

    @staticmethod
    def get_dp_str(first: str, second: str) -> str:
        return f"\\DP{{{first}}}{{{second}}}"

    def get_dp(self, first: str, second: str) -> tuple[int, str]:
        res_int = self.dp[first][second]
        res_str = Node.get_dp_str(first, second)
        return res_int, res_str

    def print_and_set_relation(
        self, first: str, second: str, relation: str, result: int
    ):
        self.dp[first][second] = result
        dp_str = Node.get_dp_str(first, second)
        print(f"{dp_str} &= {relation} = {result}\\\\")

    @staticmethod
    def get_combs_of_set(values: set[str]) -> list[set[str]]:
        combs: list[set[str]] = []
        set_size = min(2, len(values))
        for i in range(set_size + 1):
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
        self.print_and_set_relation(EMPTYSET, EMPTYSET, "0", 0)


@final
class Introduce(Node):
    new: str
    child: Node

    def __init__(self, new: str, child: Node):
        super().__init__()
        self.value = child.value.copy()
        self.value.add(new)
        self.new = new
        self.child = child

    @override
    def create_relations(self):
        print(f"\\intertext{{Introduce {self.new}}}")

        child_str = self.get_value_as_set_string(self.child.value)
        self_str = self.get_value_as_set_string(self.value)

        for comb in self.get_combs():
            comb_str = self.get_value_as_set_string(comb)
            if self.new in comb:
                no_v = comb.copy()
                no_v.remove(self.new)
                no_v_str = self.get_value_as_set_string(no_v)

                res_int, res_str = self.child.get_dp(child_str, no_v_str)
                res_str += " + 1"
                res_int += 1
            else:
                res_int, res_str = self.child.get_dp(child_str, comb_str)

            self.print_and_set_relation(self_str, comb_str, res_str, res_int)


@final
class Forget(Node):
    forget: str
    child: Node

    def __init__(self, forget: str, child: Node):
        super().__init__()
        self.value = child.value.copy()
        self.value.remove(forget)
        self.forget = forget
        self.child = child

    @override
    def create_relations(self):
        print(f"\\intertext{{Forget {self.forget}}}")

        child_str = self.get_value_as_set_string(self.child.value)
        self_str = self.get_value_as_set_string(self.value)

        for comb in self.get_combs():
            comb_str = self.get_value_as_set_string(comb)

            with_v = comb.copy()
            with_v.add(self.forget)
            with_v_str = self.get_value_as_set_string(with_v)

            comb_res_int, comb_res_str = self.child.get_dp(child_str, comb_str)
            if len(with_v) == 3:
                with_v_int = -1
                with_v_str = Node.get_dp_str(child_str, with_v_str)
            else:
                with_v_int, with_v_str = self.child.get_dp(child_str, with_v_str)

            res = f"max({comb_res_str}, {with_v_str})"
            res_int = max(comb_res_int, with_v_int)

            self.print_and_set_relation(self_str, comb_str, res, res_int)


@final
class Join(Node):
    left: Node
    right: Node

    def __init__(self, left: Node, right: Node):
        super().__init__()
        self.value = left.value.union(right.value)
        self.left = left
        self.right = right

    @override
    def create_relations(self):
        print("\\intertext{Join}")
        left_str = self.get_value_as_set_string(self.left.value)
        right_str = self.get_value_as_set_string(self.right.value)
        self_str = self.get_value_as_set_string(self.value)

        for comb in self.get_combs():
            comb_str = self.get_value_as_set_string(comb)
            left_res_int, left_res_str = self.left.get_dp(left_str, comb_str)
            right_res_int, right_res_str = self.right.get_dp(right_str, comb_str)

            res = f"{left_res_str} + {right_res_str} - |{comb_str}|"
            res_int = left_res_int + right_res_int - len(comb)

            self.print_and_set_relation(self_str, comb_str, res, res_int)


def small_sample() -> list[Node]:
    # Lecture notes from lecture 15, page 6
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

    return nodes


def big_sample() -> list[Node]:
    # Lecture 16s Drawing from the "tv board"
    nodes: list[Node] = []
    nodes.append(Leaf())  # 0
    nodes.append(Introduce("f", nodes[0]))  # 1
    nodes.append(Introduce("g", nodes[1]))  # 2
    nodes.append(Introduce("a", nodes[2]))  # 3
    nodes.append(Forget("g", nodes[3]))  # 4
    nodes.append(Introduce("d", nodes[4]))  # 5

    nodes.append(Leaf())  # 6
    nodes.append(Introduce("i", nodes[6]))  # 7
    nodes.append(Introduce("h", nodes[7]))  # 8
    nodes.append(Forget("i", nodes[8]))  # 9
    nodes.append(Introduce("f", nodes[9]))  # 10
    nodes.append(Introduce("d", nodes[10]))  # 11
    nodes.append(Forget("h", nodes[11]))  # 12
    nodes.append(Introduce("a", nodes[12]))  # 13

    nodes.append(Join(nodes[5], nodes[13]))  # 14
    nodes.append(Forget("f", nodes[14]))  # 15
    nodes.append(Introduce("c", nodes[15]))  # 16
    nodes.append(Introduce("b", nodes[16]))  # 17

    nodes.append(Leaf())  # 18
    nodes.append(Introduce("e", nodes[18]))  # 19
    nodes.append(Introduce("d", nodes[19]))  # 20
    nodes.append(Introduce("c", nodes[20]))  # 21
    nodes.append(Forget("e", nodes[21]))  # 22
    nodes.append(Introduce("b", nodes[22]))  # 23
    nodes.append(Introduce("a", nodes[23]))  # 24

    nodes.append(Leaf())  # 25
    nodes.append(Introduce("j", nodes[25]))  # 26
    nodes.append(Introduce("c", nodes[26]))  # 27
    nodes.append(Introduce("a", nodes[27]))  # 28
    nodes.append(Forget("j", nodes[28]))  # 29
    nodes.append(Introduce("d", nodes[29]))  # 30
    nodes.append(Introduce("b", nodes[30]))  # 31

    nodes.append(Join(nodes[24], nodes[31]))  # 32
    nodes.append(Join(nodes[17], nodes[32]))  # 33

    return nodes


if __name__ == "__main__":
    nodes = small_sample()
    # nodes = big_sample()

    for node in nodes:
        node.create_relations()
