import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


class BasicFunctions:
    def __init__(self):
        pass

    @staticmethod
    def model(input_x, weight, bias):
        return input_x * weight + bias

    @staticmethod
    def squared_error_cost(targets, predictions):
        samples = len(targets)

        accumulated_error = 0.0
        for target, prediction in zip(targets, predictions):
            accumulated_error += (target - prediction) ** 2
        return (1.0 / (2 * samples)) * accumulated_error

    @staticmethod
    def gradient_weight(x, y, w, b) -> float:
        m = len(x)
        accumulated_error = 0.0
        for i in range(m):
            accumulated_error += (BasicFunctions.model(x[i], w, b) - y[i]) * x[i]
        return accumulated_error / m

    @staticmethod
    def gradient_bias(x, y, w, b) -> float:
        m = len(x)
        accumulated_error = 0.0
        for i in range(m):
            accumulated_error += BasicFunctions.model(x[i], w, b) - y[i]
        return accumulated_error / m