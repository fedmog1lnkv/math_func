from matplotlib import pyplot as plt
from interpolation import *
from matrix import transportation_matrix


def draw_interpolate(data, indent=1):
    ''' Draw linear interpolation '''
    plt.title("Line interpolation")
    x, y = get_xy(data)
    plt.scatter(x, y, color='blue')
    intr_point = linear_interpolation(data)
    extr_point = linear_extrapolate(data, indent=indent)
    plt.scatter(intr_point[0], intr_point[1], color="orange")
    plt.scatter(extr_point[0], extr_point[1], color="orange")
    show_graph(x, y)


def draw_interpolate_piece_line(data):
    ''' Draw piece line interpolation by pyplot '''
    plt.title("Piece line interpolation")
    x, y = get_xy(data)
    plt.scatter(x, y, color="blue")
    points = interpolate_piece_line(data)
    interpolation_points = points[1:-1]
    extrapolation_points = [points[0], points[-1]]
    plt.scatter(transportation_matrix(interpolation_points)[0], transportation_matrix(interpolation_points)[1],
                color="orange")
    plt.scatter(transportation_matrix(extrapolation_points)[0], transportation_matrix(extrapolation_points)[1],
                color="orange")
    show_graph(x, y)


def show_graph(x, y):
    ''' Show plot '''
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


def get_xy(matrix_xy):
    ''' Return x, y arrays from matrix_xy '''
    x = transportation_matrix(matrix_xy)[0]
    y = transportation_matrix(matrix_xy)[1]
    return x, y


def draw_lagranzh(data, indent=1):
    ''' Draw Lagranzh polinomial by pyplot '''
    plt.title("Lagrange interpolation polynomial")
    arr_x = transportation_matrix(data)[0][:]
    x, y = get_xy(data)
    plt.scatter(x, y, color="blue")
    plt.axis([min(x) - 1, max(x) + indent, min(y) - indent, max(y) + indent])
    x = [i / 10 for i in range((min(arr_x) - indent) * 10, (max(arr_x) + indent) * 10 + 1)]
    y = [lagrange_interpolation_polynomial(data, x[i]) for i in range(len(x))]
    show_graph(x, y)
