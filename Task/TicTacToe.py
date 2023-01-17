from typing import NamedTuple


class Const(NamedTuple):
    DOT_EMPTY = "."
    DOT_X = "X"
    DOT_0 = "0"


CONST = Const()

game_map = [CONST.DOT_EMPTY for x in range(10)]


def is_cell_valid(position):
    return game_map[position] == CONST.DOT_EMPTY


def set_object(object, position):
    game_map[position] = object


def draw_map(game_map):
    for i in range(len(game_map)):
        game_map[i] = CONST.DOT_EMPTY

    for i in range(3):
        print(game_map[i + i * 3],
              game_map[i + i * 3],
              game_map[i + i * 3])

def players_turn(human_turn):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + human_turn + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(game_map[player_answer - 1]) not in "XO"):
                game_map[player_answer - 1] = human_turn
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(game_map):
    coordinate_for_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in coordinate_for_win:
        if game_map[each[0]] == game_map[each[1]] == game_map[each[2]]:
            return game_map[each[0]]
    return False


def start_game(game_map):
    counter = 0
    win = False
    while not win:
        draw_map(game_map)
        if counter % 2 == 0:
            players_turn("X")
        else:
            players_turn("O")
        counter += 1
        if counter > 4:
            tmp = check_win(game_map)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_map(game_map)


start_game(game_map)
