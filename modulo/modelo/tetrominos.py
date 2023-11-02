class Tetromino:
    def __init__(self, shape):
        self.shape = shape  # Matriz que contiene la figura
        self.rotation = 0  # Guarda el estado de la rotacion actual

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4  # Incrementa en la rotacion
        self.shape = list(map(list, zip(*self.shape[::-1]))) # Rota la matriz cambiando filas por columnas

    def print_tetromino(self):
        for row in self.shape:
            for cell in row:
                if cell == '@':
                    print('@', end=' ')
                else:
                    print('.', end=' ')
            print()


tetromino_I = Tetromino([
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.']
])

tetromino_O = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '@', '@', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'],
])

tetromino_T = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '@', '@', '@'],
    ['.', '.', '@', '.'],
    ['.', '.', '.', '.']
])

tetromino_S = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '.', '@', '@'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'],
])

tetromino_Z = Tetromino([
    ['.', '.', '.', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '@', '@'],
    ['.', '.', '.', '.'],
])

tetromino_J = Tetromino([
    ['.', '.', '@', '.'],
    ['.', '.', '@', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'],
])

tetromino_L = Tetromino([
    ['.', '@', '.', '.'],
    ['.', '@', '.', '.'],
    ['.', '@', '@', '.'],
    ['.', '.', '.', '.'],
])

print(" I en su estado inicial:")
tetromino_I.print_tetromino()

print("I después de una rotación:")
tetromino_I.rotate()
tetromino_I.print_tetromino()

print("I después de dos rotaciones:")
tetromino_I.rotate()
tetromino_I.print_tetromino()

print("I después de tres rotaciones:")
tetromino_I.rotate()
tetromino_I.print_tetromino()










