import numpy as np


def normalize(data: np.array):
    """
    Normalize the data between 0 and 1
    Parameters
    ----------
    data : np. Array
        The data to be normalized
    Returns
    -------
    np. Array
        The normalized data between 0 and 1
    int
        The maximum value of the data
    """
    data_max = np.max(data)
    return data / data_max, data_max


def mean_normalize(data: np.array):
    """
    Normalize the data between -1 and 1
    Parameters
    ----------
    data : np. Array
        The data to be normalized
    Returns
    -------
    np. Array
        The normalized data between -1 and 1
    float
        The mean of the data
    float
        The range of the data
    """
    data_mean = np.mean(data)
    data_range = np.max(data) - np.min(data)
    return (data - data_mean) / data_range, data_mean, data_range


def z_score_normalize(data: np.array):
    """
    Normalize the data using the z-score
    Parameters
    ----------
    data : np. Array
        The data to be normalized
    Returns
    -------
    np. Array
        The normalized data using the z-score
    float
        The mean of the data
    float
        The standard deviation of the data
    """
    data_mean = np.mean(data)
    data_std = np.std(data)
    return (data - data_mean) / data_std, data_mean, data_std
