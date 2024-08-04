import numpy as np
import matplotlib.pyplot as plt


def model(input_x, weight, bias):
    return input_x * weight + bias


def squared_error_cost(targets, predictions):
    samples = len(targets)
    cost = np.sum((targets - predictions) ** 2)
    return (1.0 / (2 * samples)) * cost


def plot_multivariable_gradient_descent(iterations, cost_history, weight_history, bias_history, feature_names):
    # plot the iterations vs cost
    plt.subplots(1, 3, figsize=(30, 10))

    plt.subplot(1, 3, 1)
    plt.plot(range(iterations), cost_history)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')

    # plot the iterations vs weight
    plt.subplot(1, 3, 2)
    for idx in range(len(feature_names)):
        plt.plot(range(iterations), weight_history[:, idx], label=feature_names[idx])
    plt.xlabel('Iterations')
    plt.ylabel('Weight')
    plt.legend(loc='upper right')  # Add legend to distinguish each weight

    # plot the iterations vs bias
    plt.subplot(1, 3, 3)
    plt.plot(range(iterations), bias_history)
    plt.xlabel('Iterations')
    plt.ylabel('Bias')

    plt.tight_layout()
    plt.show()
