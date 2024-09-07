# custom Neural Network implementation in Python
import numpy as np


def sigmoid(input_x):
    """
    Sigmoid activation function
    Parameters
    ----------
    input_x : float
        The input data
    Returns
    -------
    float
        The output of the sigmoid activation function
    """
    return 1 / (1 + np.exp(-input_x))


def dense(a_in, w, b):
    """
    Dense layer
    Parameters
    ----------
    a_in : np. Array
        The input data
    w : np. Array
        The weights
    b : np. Array
        The bias
    Returns
    -------
    np. Array
        The output of the dense layer
    """
    units = w.shape[1]
    a_out = np.zeros(units)
    for i in range(units):
        a_out[i] = sigmoid(np.dot(w[:, i], a_in) + b[i])
    return a_out


def sequential_model(x):
    w1 = np.array(
        [[1, -3, 5],
         [-2, 4, -6]])
    b1 = np.array([-1, 1, 2])
    a1 = dense(x, w1, b1)
    return a1


x = np.array([200, 17])

print(sequential_model(x))


# vectorized Neural Network implementation in Python

def dense_vectorized(a_in, w, b):
    Z = np.matmul(a_in, w) + b
    return sigmoid(Z)


x = np.array([[200, 17]])
w = np.array([[1, -3, 5], [-2, 4, -6]])
b = np.array([[-1, 1, 2]])

print(dense_vectorized(x, w, b))
