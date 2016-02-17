from __future__ import division, print_function
import time

from IPython import display
import matplotlib.pyplot as plt
import networkx as nx


def animate_network(ax, weights, activations, dt, **kwargs):
    """
    Animate a dynamically changing network in the output of a Jupyter cell.

    :param weights: weight matrix (or list of weight matrices if changing)
    :param activations: array of activations
    :param dt:
    :param kwargs:
    :return:
    """

    # make a graph
    g = nx.from_numpy_matrix(weights.T, create_using=nx.DiGraph())

    # get positions
    pos = nx.spring_layout(g)

    for activation in activations:
        ax.cla()
        nx.draw(g, ax=ax, pos=pos, node_color=activation, **kwargs)
        display.clear_output(wait=True)
        display.display(plt.gcf())
        time.sleep(dt)