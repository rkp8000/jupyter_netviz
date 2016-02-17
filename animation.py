from __future__ import division, print_function
import time

from IPython import display
import matplotlib.pyplot as plt
import networkx as nx


def animate_network(ax, weights, activations, dt, pos=nx.spring_layout, **kwargs):
    """
    Animate a dynamically changing network in the output of a Jupyter cell.

    :param weights: weight matrix
    :param activations: array of activations
    :param dt: timestep to wait before updating display
    :param kwargs: see https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html for options
    :return:
    """

    # make a graph
    g = nx.from_numpy_matrix(weights.T, create_using=nx.DiGraph())

    # get positions
    if not isinstance(pos, dict):
        pos = pos(g)

    for activation in activations:
        ax.cla()
        # get edge colors
        edge_colors = [activation[edge[0]] for edge in g.edges()]
        nx.draw(g, ax=ax, pos=pos, node_color=activation, edge_color=edge_colors, **kwargs)
        display.clear_output(wait=True)
        display.display(plt.gcf())
        time.sleep(dt)