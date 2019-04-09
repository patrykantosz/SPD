import numpy
import random
import copy
from math import exp
import time

class Annealing:
    def __init__(self):
        self.first_seq = []

    def makespan(self, sequence_order, times, number_of_machines):
        c_max = numpy.zeros((len(sequence_order) + 1, number_of_machines))
        for index in range(1, len(sequence_order) + 1):
            c_max[index][0] = c_max[index - 1][0] + times[sequence_order[index - 1]][0]
        for index in range(1, number_of_machines):
            for index2 in range(1, len(sequence_order) + 1):
                c_max[index2][index] = max(c_max[index2][index - 1], c_max[index2 - 1][index]) \
                                       + times[sequence_order[index2 - 1]][index]
        return c_max[-1][-1]  # return only last element in array

    def make_natural_seq(self, number_of_tasks):
        for i in range(0, number_of_tasks):
            self.first_seq.append(i)

    def make_random_swap(self, number_of_tasks):
        new_seq = copy.deepcopy(self.first_seq)
        first_index = random.randrange(0, number_of_tasks)
        while(True):
            second_index = random.randrange(0, number_of_tasks)
            if(second_index != first_index):
                break
        new_seq[first_index], new_seq[second_index] = new_seq[second_index], new_seq[first_index]
        return new_seq

    def make_random_insert(self, number_of_tasks):
        new_seq = copy.deepcopy(self.first_seq)
        index_to_move = random.randrange(0, number_of_tasks)
        while(True):
            index_where_to_move = random.randrange(0, number_of_tasks)
            if(index_to_move != index_where_to_move):
                break
        new_seq.insert(index_where_to_move, new_seq.pop(index_to_move))
        return new_seq


    def get_probability(self, pi_0, pi_prim, temperature):
        if(pi_prim < pi_0):
            return 1
        else:
            return exp((pi_0 - pi_prim) / temperature)

    def get_probability_test_version(self, pi_0, pi_prim, temperature):
            return exp((pi_0 - pi_prim) / temperature)

    def make_decision(self, probability):
        tmp = random.random()
        if(probability > tmp):
            return True
        else:
            return False

    def do_cooling(self, temperature, u):
        return u * temperature

    def simulated_annealing(self, tasks, number_of_machines, number_of_tasks, type_of_random_move, u = 0.24, start_temp = 2000, stop_temp = 1, probability_version = 1, sequence = []):
        self.first_seq = []
        start = time.time()
        #step 1 initialization
        if not sequence:
            self.make_natural_seq(number_of_tasks)
        else:
            self.first_seq = sequence
        pi_0 = self.makespan(self.first_seq, tasks, number_of_machines)
        temperature = start_temp
        while(temperature > stop_temp):
            #step 2 generating move
            if(type_of_random_move == "swap"):
                new_seq = self.make_random_swap(number_of_tasks)
            else:
                new_seq = self.make_random_insert(number_of_tasks)
            pi_0 = self.makespan(self.first_seq, tasks, number_of_machines)
            pi_prim = self.makespan(new_seq, tasks, number_of_machines)

            #step 3 do or not do
            if probability_version == 1:
                probability = self.get_probability(pi_0, pi_prim, temperature)
            else:
                probability = self.get_probability_test_version(pi_0, pi_prim, temperature)
            if self.make_decision(probability):
                self.first_seq = copy.deepcopy(new_seq)

            #step 4 cooling
            temperature -= self.do_cooling(temperature, u)
        stop = time.time()
        return self.makespan(self.first_seq, tasks, number_of_machines), (stop-start)






