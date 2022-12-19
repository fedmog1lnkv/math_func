from matplotlib import pyplot as plt
from math import *
from maclaurin import *


def show_graph(x, y, x_data, y_data):
    plt.ylim(ymax=max(y_data))
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(x_data, y_data, color="orange")
    plt.scatter(x, y, color="red")
    plt.grid()
    plt.show()


def draw_exp(x, n):
    ''' Draws an exponent on the Maclaurin series using pyplot '''
    x_data = [i / 10 for i in range(-50, 50)]
    y_exp = [exp(X) for X in x_data]
    plt.plot(x_data, y_exp, color="blue")

    y_data = [maclaurin_exp(X, n) for X in x_data]
    y_dot = maclaurin_exp(x, n)

    show_graph(x, y_dot, x_data, y_data)


def draw_cos(x, n):
    ''' Draws a cosine along the Maclaurin series using pyplot '''
    x_data = [i / 10 for i in range(-50, 50)]
    y_cos = [cos(X) for X in x_data]
    plt.plot(x_data, y_cos, color="blue")

    y_data = [maclaurin_cos(X, n) for X in x_data]
    y_dot = maclaurin_cos(x, n)

    show_graph(x, y_dot, x_data, y_data)


def draw_sin(x, n):
    ''' Draws a sinusoid along the Maclaurin series using pyplot '''
    x_data = [i / 10 for i in range(-50, 50)]
    y_sin = [sin(X) for X in x_data]
    plt.plot(x_data, y_sin, color="blue")

    y_data = [maclaurin_sin(X, n) for X in x_data]
    y_dot = maclaurin_sin(x, n)

    show_graph(x, y_dot, x_data, y_data)
