def pi_montecarlo(number):
    import numpy as np

    n = 256556
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    dist = np.sqrt(x**2 + y**2)
    circ = dist[dist < 1]
    pi = 4.0 * circ.size / n
    print(f"El valor de pi es: {pi}")