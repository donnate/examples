"""
Plot the result of optimal quantization of the von Mises Fisher distribution
on the sphere
"""

import matplotlib.pyplot as plt

import geomstats.visualization as visualization
import quantization.optimal_quantization as oq

from geomstats.hypersphere import Hypersphere

SPHERE2 = Hypersphere(dimension=2)
METRIC = SPHERE2.metric
N_POINTS = 1000
N_CENTERS = 4
N_REPETITIONS = 20
KAPPA = 10


def main():
    points = SPHERE2.random_von_mises_fisher(kappa=KAPPA, n_samples=N_POINTS)

    centers, weights, clusters, n_steps = oq.optimal_quantization(
                points=points, metric=METRIC, n_centers=N_CENTERS,
                n_repetitions=N_REPETITIONS
                )

    plt.figure(0)
    ax = plt.subplot(111, projection="3d", aspect="equal")
    visualization.plot(points=centers, ax=ax, space='S2', c='r')
    plt.show()

    plt.figure(1)
    ax = plt.subplot(111, projection="3d", aspect="equal")
    sphere = visualization.Sphere()
    sphere.draw(ax=ax)
    for i in range(N_CENTERS):
        sphere.draw_points(ax=ax, points=clusters[i])


if __name__ == "__main__":
    main()
