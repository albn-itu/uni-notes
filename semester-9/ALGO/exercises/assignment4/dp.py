import itertools

EMPTYSET = "\\emptyset"


class Node:
    value = set()

    @staticmethod
    def get_value_as_set_string(values):
        if not values:
            return EMPTYSET
        return "\\{" + ", ".join(sorted(list(values))) + "\\}"

    @staticmethod
    def print_dp(first, second, result):
        print(f"DP[{first}][{second}] &= {result} = \\\\")

    @staticmethod
    def get_combs_of_set(values):
        combs = []
        for i in range(len(values) + 1):
            combs.extend(list(itertools.combinations(values, i)))
        combs = [set(comb) for comb in combs]

        return combs

    def get_combs(self):
        return Node.get_combs_of_set(self.value)

    def create_relations(self):
        pass


class Leaf(Node):
    def create_relations(self):
        print("\\intertext{Leaf}")
        Node.print_dp(EMPTYSET, EMPTYSET, "0")


class Introduce(Node):
    def __init__(self, new, child):
        self.value = child.value.copy()
        self.value.add(new)
        self.new = new
        self.child = child

    def create_relations(self):
        print(f"\\intertext{{Introduce {self.new}}}")
        combs = self.get_combs()

        child_str = self.get_value_as_set_string(self.child.value)
        for comb in combs:
            comb_str = self.get_value_as_set_string(comb)
            if self.new in comb:
                no_v = comb.copy()
                no_v.remove(self.new)
                relations = []
                for subcomb in Node.get_combs_of_set(no_v):
                    subcomb_str = self.get_value_as_set_string(subcomb)
                    relations.append(f"DP[{child_str}][{subcomb_str}]")

                if len(relations) == 1:
                    res_str = relations[0] + " + 1"
                else:
                    res_str = "min(" + ", ".join(relations) + ") + 1"
            else:
                res_str = f"DP[{child_str}][{comb_str}]"

            Node.print_dp(
                self.get_value_as_set_string(self.value),
                comb_str,
                res_str
            )


class Forget(Node):
    def __init__(self, forget, child):
        self.value = child.value.copy()
        self.value.remove(forget)
        self.forget = forget
        self.child = child

    def create_relations(self):
        print(f"\\intertext{{Forget {self.forget}}}")
        child_str = self.get_value_as_set_string(self.child.value)

        combs = self.get_combs()
        for comb in combs:
            comb_str = self.get_value_as_set_string(comb)

            if comb is None:
                comb = set()
            with_v = comb.copy()
            with_v.add(self.forget)
            with_v_str = self.get_value_as_set_string(with_v)

            res_str = "min(DP[{child_str}][{comb_str}], DP[{child_str}][{with_v_str}])".format(
                child_str=child_str,
                comb_str=comb_str,
                with_v_str=with_v_str
            )

            Node.print_dp(
                self.get_value_as_set_string(self.value),
                comb_str,
                res_str
            )


class Join(Node):
    def __init__(self, left, right):
        self.value = left.value.copy()
        self.value.union(right.value)
        self.left = left
        self.right = right

    def create_relations(self):
        print("\\intertext{Join}")
        left_str = self.get_value_as_set_string(self.left.value)
        right_str = self.get_value_as_set_string(self.right.value)

        combs = self.get_combs()
        for comb in combs:
            comb_str = self.get_value_as_set_string(comb)

            res_str = "DP[{left_str}][{comb_str}] + DP[{right_str}][{comb_str}]) - |{comb_str}|".format(
                left_str=left_str,
                right_str=right_str,
                comb_str=comb_str,
            )

            Node.print_dp(
                self.get_value_as_set_string(self.value),
                comb_str,
                res_str
            )


if __name__ == "__main__":
    nodes = []
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
