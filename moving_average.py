def calculate_moving_average(data, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(data, weights, 'valid')
    return smas