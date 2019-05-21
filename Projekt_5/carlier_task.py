import copy
import math


class Carlier_Task:
    def __init__(self, tasks):
        self.U = None
        self.UB = math.inf
        self.pi = []
        self.opt_pi = []
        self.a = None
        self.b = None
        self.c = None
        self.tasks = copy.deepcopy(tasks)