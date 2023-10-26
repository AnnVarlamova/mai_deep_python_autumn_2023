class TicTacToe:

    def __init__(self, dim=3):
        self.side = "x"
        self.dim = dim
        self.matrix = []
        self.i = 0
        self.j = 0
        for i in range(self.dim):
            to_append = []
            for j in range(self.dim):
                to_append.append('*')
            self.matrix.append(to_append)

    def show_board(self):
        print(end='  ')
        for i in range(self.dim):
            if i == 0:
                for j in range(self.dim):
                    print(j + 1, end=' ')
                print()
            for j in range(self.dim):
                if j == 0:
                    print(i + 1, end=' ')
                print(self.matrix[i][j], end=' ')
            print()

    def validate_input(self, i, j):
        return (i >= 0 and j >= 0) and (i < self.dim and j < self.dim) and self.matrix[i][j] == '*'

    def enter_coordinates(self):
        i, j = 0, 0
        while not self.validate_input(i - 1, j - 1):
            print(f"Player for {self.side},")
            print(f"Enter two coordinates from 1 to {self.dim}, for example '1 1'")
            self.show_board()
            try:
                i, j = map(int, input().split())
            except ValueError:
                print("Incorrect input! Try again!")
        self.matrix[i - 1][j - 1] = self.side
        return i - 1, j - 1

    def check_side(self):
        game_type = input()
        if game_type == 'x' or game_type == 'X':
            self.side = "x"
            return True
        elif game_type == '0' or game_type == 'o' or game_type == 'O':
            self.side = "0"
            return True
        else:
            return False

    def choose_side(self):
        # просим выбрать за кого играть, пока игрок не выберет нормально
        print('Choose a side: x or 0')
        side_is_chosen = self.check_side()
        while not side_is_chosen:
            print("Enter 'x' or '0'")
            side_is_chosen = self.check_side()

    def check_winner(self, i, j):
        k_i = 0     # совпадают символы в строке
        k_j = 0     # в столбце
        k_main = 0  # на главной диагонали
        k_side = 0  # на побочной диагонали
        for k in range(self.dim - 1):
            if self.matrix[i][k] == self.matrix[i][k + 1]:  # строка
                k_i += 1
            if self.matrix[k][j] == self.matrix[k + 1][j]:  # столбец
                k_j += 1
        if i == j:
            for k in range(self.dim - 1):                   # главная диагональ
                if self.matrix[k][k] == self.matrix[k + 1][k + 1]:
                    k_main += 1
        if i + j == self.dim - 1:                           # побочная диагональ
            for k in range(self.dim - 1):
                if self.matrix[k][self.dim - k - 1] == self.matrix[k + 1][self.dim - k - 2]:
                    k_side += 1

        return k_i == self.dim - 1 or k_j == self.dim - 1 or \
               k_main == self.dim - 1 or k_side == self.dim - 1

    def change_side(self):  # для осуществления смены игрока
        if self.side == "x":
            self.side = "0"
        else:
            self.side = "x"

    def play_game(self):  # здесь логика игры
        self.choose_side()
        game_over = False
        steps_number = 1  # нужно для ничьей
        while not game_over:                     # пока никто не выиграл
            if steps_number > self.dim ** 2:     # если сделано макс кол-во ходов
                break
            i, j = self.enter_coordinates()      # игрок делает ход
            game_over = self.check_winner(i, j)  # проверка не выиграл ли
            self.change_side()                   # смена игрока
            steps_number += 1
        self.show_board()
        if game_over:                           # кто-то выиграл
            self.change_side()                  # тк игрока в цикле поменяли
            return True
        else:
            return False                        # ничья


def input_dimension():
    dim = 0
    while not (3 <= dim <= 10):
        print("Enter the dimension (3 <= number <= 10):")
        try:
            dim = int(input())
        except ValueError:
            print("It's not integer!")
    return dim


if __name__ == "__main__":
    n = input_dimension()
    game = TicTacToe(n)
    winner = game.play_game()
    if winner:
        print(f"{game.side} won!")
    else:
        print("Draw!")
