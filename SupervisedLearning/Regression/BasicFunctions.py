import numpy as np


class BasicFunctions:
    def __init__(self):
        pass

    @staticmethod
    def model(input_x, weight, bias):
        return input_x * weight + bias

    @staticmethod
    def squared_error_cost(targets, predictions):
        samples = len(targets)
        cost = np.sum((targets - predictions) ** 2)
        return (1.0 / (2 * samples)) * cost
