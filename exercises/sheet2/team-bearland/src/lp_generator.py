#!/usr/bin/python3
import gurobipy as gp
import numpy as np
import sys
from gurobipy import GRB

class PointConfig:
    def __init__(self, file_path):
        self.points = np.genfromtxt(file_path, delimiter=' ')
        self.num_points = np.size(self.points) / np.size(self.points[0])
        self.dim = np.size(self.points[0])

    def __repr__(self):
        return "PointConfig()"

    def __str__(self):
        _str = "Point Configuration:\n"
        _str += " - Number of points: {}\n".format(self.num_points)
        _str += " - Point dimension: {}\n".format(self.dim)
        _str += " - Raw points:\n{}\n".format(self.points)
        return _str


class Triangulation:
    def __init__(self, file_path):
        # TODO: should we subtract one so that we can index points directly?
        self.facets = np.genfromtxt(file_path, delimiter=' ')

    def __repr__(self):
        return "Triangulation()"

    def __str__(self):
        _str = "Point Configuration:\n"
        _str += " - Raw points:\n{}\n".format(self.facets)
        return _str


def usage():
    print("LP File Generator:")
    print("USAGE: ./lp_generator.py <file.vertices> <file.triangulation>")


def generate_lp(point_config, triangulation):
    print(point_config)
    print(triangulation)
    model = gp.Model('folding')
    # TODO: Objective Function?
    # Add Variables
    var = model.addVars(point_config.dim, vtype=GRB.INT, name='y')
    var = model.addVars(point_config.num_points, vtype=GRB.INT, name='w')
    # Add Constraints
    #model.addConstrs(
    model.write('folding.lp')

if __name__=="__main__":
    if (len(sys.argv) != 3 or sys.argv[1].split('.')[-1] != "vertices"
            or sys.argv[2].split('.')[-1] != "triangulation"):
        usage()
    else:
        point_config = PointConfig(sys.argv[1])
        triangulation = Triangulation(sys.argv[2])
        generate_lp(point_config, triangulation)
