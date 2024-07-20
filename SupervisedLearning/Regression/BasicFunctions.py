import numpy as np


def model(input_x, weight, bias):
    return input_x * weight + bias


def squared_error_cost(targets, predictions):
    samples = len(targets)

    accumulated_error = 0.0
    for target, prediction in zip(targets, predictions):
        accumulated_error += (target - prediction) ** 2
    return (1.0 / (2 * samples)) * accumulated_error


