from math import sqrt
import pandas as pd


class RectBeam:
    """This class takes a beam element and make calculation of inertia and the section area."""

    all = []

    # I need to work on the beam class to use it to calculate the length of the beam without entering it.
    def __init__(self, material: str, young_modulus: float, base: float,
                 height: float, st_node: int, end_node: int):
        assert base >= 0, f"The base {base} is not greater or equal to 0."
        assert height >= 0, f"The height {height} is not greater or equal to 0."
        assert young_modulus >= 0, f"The Young modulus {young_modulus} is not greater or equal to 0."
        assert st_node > 0, f"The starting node {st_node} is not greater than 0."
        assert end_node > 0, f"The ending node {end_node} is not greater than 0."

        self.material = material
        self.young_modulus = young_modulus
        self.base = base
        self.height = height
        self.st_node = st_node
        self.end_node = end_node

        RectBeam.all.append(self)

    def calc_area(self):
        return self.base * self.height

    def calc_inertia(self):
        return round((self.base * self.height ** 3) / 12, 3)

    @staticmethod
    def calc_run_rise(st_n, e_n):
        n_data = pd.read_csv('Node_list.csv')
        n_number = list(n_data['Node number'])
        x_pos = list(n_data['Position X'])
        y_pos = list(n_data['Position Y'])
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0

        for i in range(len(n_number)):
            if i+1 == st_n:
                x1 = x_pos[i]
                y1 = y_pos[i]
            if i+1 == e_n:
                x2 = x_pos[i]
                y2 = y_pos[i]

        return (x2 - x1), (y2 - y1)

    def calc_length(self):
        a, b = self.calc_run_rise(self.st_node, self.end_node)
        return round(sqrt(a ** 2 + b ** 2), 3)

    def __repr__(self):
        return f"Beam({self.material}, {self.young_modulus}, {self.base}" \
               f", {self.height}, {self.st_node}, {self.end_node},{self.calc_length()}," \
               f" {self.calc_area()}, {self.calc_inertia()})"


class TrussNode:
    """This class takes the characteristics of a truss node."""

    all = []

    def __init__(self, node_num: int, x_pos: float, y_pos: float, x_reaction: bool, y_reaction: bool):
        assert node_num > 0, f"The node number {node_num} is not greater than 0."
        assert x_pos >= 0, f"The position on the X axis {x_pos} is not greater or equal to 0."
        assert y_pos >= 0, f"The position on the Y axis {y_pos} is not greater or equal to 0."

        self.node_num = node_num
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_reaction = x_reaction
        self.y_reaction = y_reaction

        TrussNode.all.append(self)

    def __repr__(self):
        return f"Node({self.node_num}, {self.x_pos}, {self.y_pos}, {self.x_reaction}, {self.y_reaction})"


class TrussLoad:
    """This class takes the characteristics of a truss load."""

    all = []

    def __init__(self, node_app: int, x_load: float, y_load: float):
        assert node_app > 0, f"The node number {node_app} is not greater than 0."

        self.node_app = node_app
        self.x_load = x_load
        self.y_load = y_load

        TrussLoad.all.append(self)

    def __repr__(self):
        return f"Load({self.node_app}, {self.x_load}, {self.y_load})"
