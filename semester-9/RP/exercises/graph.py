import numpy as np
import sys
from copy import deepcopy


class Edge:
    def __init__(self, start, end, lower, upper, flow=0):
        self.start = start
        self.end = end
        self.lower = lower
        self.upper = upper
        self.flow = flow

        self.verify()

    def __str__(self):
        return f"({self.start}, {self.end}, {self.lower}, {self.upper}, {self.flow})"

    def __repr__(self):
        return self.__str__()

    def verify(self):
        if self.lower > self.upper:
            raise ValueError(
                "Lower bound must be less than or equal to upper bound")

        if self.flow < self.lower or self.flow > self.upper:
            print("Flow must be within bounds", self, file=sys.stderr)

    def get_dot(self, show_label=True, show_flow=True):
        def construct(label):
            return f'{self.start} -> {self.end} [label="{label}"];'

        if not show_label:
            return construct("")
        if show_flow:
            return construct(f'f={self.flow}\\n{self.lower}/{self.upper}')
        else:
            return construct(f'{self.lower}/{self.upper}')

    def get_tikz(self, show_label=True, show_flow=True, path_att=None):
        node_att = 'font=\\footnotesize,sloped,midway'

        lines = []

        lines.append(f"\\draw[myarrow] ({self.start})")
        if path_att:
            lines.append(f'to[{path_att}]')
        else:
            lines.append('to')

        if show_label:
            lines.append(
                f'node[{node_att}, below] {{{self.lower}/{self.upper}}}')
            if show_flow:
                lines.append(f'node[{node_att}, above] {{{self.flow}}}')

        lines.append(f'({self.end});')
        return " ".join(lines)


class Graph:
    def __init__(self, nodes, edges, demands):
        self.nodes = nodes
        self.edges = edges
        self.demands = demands

        self.verify()

    def __str__(self):
        return f"Graph(nodes={self.nodes}, edges={self.edges}, demands={self.demands})"

    def __repr__(self):
        return self.__str__()

    def verify(self):
        if np.sum(self.demands) != 0:
            raise ValueError("Demands must sum to zero")

        if np.shape(self.demands)[0] != self.nodes:
            raise ValueError(
                "Demands must have the same number of elements as nodes")

        for edge in self.edges:
            edge.verify()

    def get_edge_vertex_incidence_matrix(self):
        B = np.zeros((len(self.edges), self.nodes))
        for i, edge in enumerate(self.edges):
            B[i, edge.start] = 1
            B[i, edge.end] = -1
        return B

    def add_node(self, demand):
        self.nodes += 1
        self.demands = np.pad(self.demands, (0, 1),
                              'constant', constant_values=(demand, 0))

        self.verify()

    def add_edge(self, edge):
        self.edges.append(edge)
        self.verify()

    def get_upper(self):
        return np.array([edge.upper for edge in self.edges])

    def get_dot(self, show_flow=True, edges_to_label=None, vertex_names=None):
        lines = []

        for i in range(self.nodes):
            if vertex_names and vertex_names[i]:
                lines.append(f'{i} [label="{vertex_names[i]}"];')
            else:
                lines.append(f'{i} [label="{i}"];')

        for i, edge in enumerate(self.edges):
            should_show = not edges_to_label or edges_to_label[i]

            lines.append(edge.get_dot(
                should_show,
                show_flow,
            ))

        return lines

    def get_tikz(self, node_positions, show_flow=True, edges_to_label=None, vertex_names=None, path_att=None):
        lines = []

        for i in range(self.nodes):
            vertex_def = ['\\node[main]']

            vertex_def.append(f'({i})')

            if node_positions and node_positions[i]:
                vertex_def.append(f'[{node_positions[i]}]')

            vertex_name = f'${i}$'
            if vertex_names and vertex_names[i]:
                vertex_name = f'${vertex_names[i]}$'

            vertex_def.append(f'{{{vertex_name}}};')

            lines.append(" ".join(vertex_def))

        for i, edge in enumerate(self.edges):
            should_show = not edges_to_label or edges_to_label[i]
            path_at = path_att[i] if path_att else None

            lines.append(edge.get_tikz(
                should_show,
                show_flow,
                path_at
            ))

        return lines


def compute_g_tilde(g):
    g_tilde = deepcopy(g)
    g_tilde.add_edge(Edge(g.nodes - 1, 0, 0, sum(g.get_upper())))
    for i, edge in enumerate(g_tilde.edges):
        edge.flow = (edge.lower + edge.upper) / 2

    flow = np.array([edge.flow for edge in g_tilde.edges])
    B = g_tilde.get_edge_vertex_incidence_matrix()
    print(B, file=sys.stderr)
    dhat = np.dot(B.transpose(), flow)

    first_d = 2 * (dhat - g.demands)
    second_d = 2 * (g.demands - dhat)

    g_tilde.add_node(0)
    v_star = g_tilde.nodes - 1

    for node in range(g.nodes):
        n_dhat = dhat[node]
        n_demand = g.demands[node]
        if n_dhat > n_demand:
            g_tilde.add_edge(Edge(
                v_star,
                node,
                0,
                first_d[node],
                n_dhat - n_demand
            ))
        elif n_dhat < n_demand:
            g_tilde.add_edge(Edge(
                node,
                v_star,
                0,
                second_d[node],
                n_demand - n_dhat
            ))

    return g_tilde


def get_dot(g, show_flow=False, edges_to_label=None, vertex_names=None):
    lines = []
    lines.append("rankdir=LR;")
    lines.extend(g.get_dot(show_flow, edges_to_label, vertex_names))
    lines = ["    " + line for line in lines]

    dot = "digraph G {\n"
    dot += "\n".join(lines)
    dot += "\n}"

    return dot


def get_tikz(g, node_positions, show_flow=False, edges_to_label=None, vertex_names=None, path_att=None):
    lines = []

    lines.append("""
\\documentclass{standalone}
\\usepackage{tikz}
\\usetikzlibrary{arrows.meta, positioning}
\\begin{document}
\\begin{tikzpicture}[
    node distance={15mm},
    thick,
    main/.style = {
        draw,
        circle
    },
    myarrow/.style={
        -Stealth
    }
]
     """)

    tikz_lines = g.get_tikz(
        node_positions,
        show_flow=show_flow,
        edges_to_label=edges_to_label,
        vertex_names=vertex_names,
        path_att=path_att
    )
    tikz_lines = ["  " + line for line in tikz_lines]
    lines.extend(tikz_lines)

    lines.append("\\end{tikzpicture}")
    lines.append("\\end{document}")

    return "\n".join(lines)


def base_graph():
    return Graph(
        6,
        [
            Edge(0, 1, 2, 8),
            Edge(0, 2, 1, 9),
            Edge(1, 3, 1, 4),
            Edge(1, 2, 0, 3),
            Edge(2, 3, 2, 5),
            Edge(2, 4, 1, 8),
            Edge(3, 4, 4, 8),
            Edge(3, 5, 0, 7),
            Edge(4, 5, 4, 10),
        ],
        # np.array([-12, 2, 1, 1, 3, 5])
        np.array([0, 0, 0, 0, 0, 0])
    )


def paper_graph1():
    return Graph(
        6,
        [
            Edge(0, 1, 0, 1),
            Edge(0, 3, 0, 4),
            Edge(0, 2, 0, 1),
            Edge(1, 4, 0, 3),
            Edge(3, 1, 0, 2),
            Edge(2, 5, 0, 3),
            Edge(3, 5, 0, 1),
            Edge(4, 5, 0, 3),
        ],
        np.array([-5, 0, 0, 0, 0, 5])
    )


def paper_graph2():
    return Graph(
        6,
        [
            Edge(0, 1, 0, 1),
            Edge(0, 3, 0, 4),
            Edge(2, 0, 0, 1),
            Edge(1, 4, 0, 3),
            Edge(3, 1, 0, 2),
            Edge(5, 2, 0, 3),
            Edge(5, 3, 0, 1),
            Edge(4, 5, 0, 3),
        ],
        np.array([-5, 0, 0, 0, 0, 5])
    )


def render_base_graph():
    g = base_graph()
    g_tilde = compute_g_tilde(g)
    print(g, file=sys.stderr)
    print(g_tilde, file=sys.stderr)

    tikz = get_tikz(
        g,
        [
            None,
            'above right=of 0',
            'below right=of 0',
            'right=of 1',
            'right=of 2',
            'below right=of 3',
        ],
        show_flow=True,
        vertex_names=[None, None, None, None, None, None, 'v*']
    )
    # print(tikz)

    original_edges = [False] * len(g.edges)
    new_edges = [True] * (len(g_tilde.edges) - len(g.edges))

    original_path_att = [None] * len(g.edges)

    tikz = get_tikz(
        g_tilde,
        [
            None,
            'above right=of 0',
            'below right=of 0',
            'right=of 1',
            'right=of 2',
            'below right=of 3',
            'below right=of 2'
        ],
        edges_to_label=original_edges + new_edges,
        show_flow=True,
        vertex_names=[None, None, None, None, None, None, 'v*'],
        path_att=original_path_att + [
            'out=90,in=90,looseness=1.5',
            'out=-90,in=180',
            'out=120,in=-45',
            None,
            'out=-45,in=0',
            None,
            'out=-20, in=-70',
        ]
    )
    print(tikz)


def render_paper_graph(num):
    if num == 1:
        g = paper_graph1()
    else:
        g = paper_graph2()
    g_tilde = compute_g_tilde(g)

    tikz = get_tikz(
        g,
        [
            None,
            'above right=of 0',
            'below right=of 0',
            'right=of 0',
            'right=of 1',
            'right=of 2',
        ],
        show_flow=True,
        vertex_names=['1', '2', '3', '4', '5', '6', 'v*']
    )
    print(tikz)

    original_edges = [False] * len(g.edges)
    new_edges = [True] * (len(g_tilde.edges) - len(g.edges))

    original_path_att = [None] * len(g.edges)

    tikz = get_tikz(
        g_tilde,
        [
            None,
            'above right=of 0',
            'below right=of 0',
            'right=of 1',
            'right=of 2',
            'below right=of 3',
            'below right=of 2'
        ],
        edges_to_label=original_edges + new_edges,
        show_flow=True,
        vertex_names=[None, None, None, None, None, None, 'v*'],
        path_att=original_path_att + [
            'out=-90,in=180',
            'out=120,in=-45',
            None,
            'out=-45,in=0',
            None,
        ]
    )
    # print(tikz)


if __name__ == '__main__':
    render_base_graph()
