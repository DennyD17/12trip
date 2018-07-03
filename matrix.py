from random import randint
import argparse


def matrix_spiral_output(matrix):
    """
    :param matrix: square matrix with odd number of elements on each side
    :return: list of matrix elements taken by spiral method from center
    """
    result = []
    down, up, left, right = (1, 0), (-1, 0), (0, -1), (0, 1)
    turn = {left: down, down: right, right: up, up: left}
    i = 0
    x = y = int(len(matrix)/2)
    initial_turn = up
    while i < len(matrix) ** 2:
        result.append(matrix[x][y])
        matrix[x][y] = None
        new_x = x + turn[initial_turn][0]
        new_y = y + turn[initial_turn][1]
        if matrix[new_x][new_y] is not None:
            x, y = new_x, new_y
            initial_turn = turn[initial_turn]
        else:
            x += initial_turn[0]
            y += initial_turn[1]
        i += 1
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='length of matrix side.')
    args = parser.parse_args()
    n = args.n
    if not n:
        raise Exception('Please use -n argument to input length of matrix side.')
    if args.n < 2:
        parser.error('n must be bigger than 2.')
    my_matrix = [[randint(0, 99) for j in range(2 * n - 1)] for i in range(2 * n - 1)]
    [print(' '.join([str(elem) if elem > 9 else '0' + str(elem) for elem in row])) for row in my_matrix]
    print(', '.join(map(str, matrix_spiral_output(my_matrix))))
