from matplotlib import pyplot as plt
from approximation import *
from interpolation.graphs import get_xy, show_graph


def draw_approximation(matrix, vector_x):
    ''' Draw linear approximation by pyplot '''
    plt.title("Approximation")
    line = linear_approximation(matrix, vector_x)
    x, y = get_xy(line)
    plt.axline((x[0], y[0]), (x[-1], y[-1]), color='blue')

    plt.scatter(x, y, color="orange")

    x, y = get_xy(matrix)
    plt.scatter(x, y, color="blue")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

def draw_approximation_graph_example():
    ''' Draw example linear approximation '''
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [1, 3, 5]
    draw_approximation(data_xy, x)