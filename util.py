from models.player import Player
from models.snakes import Snake
from models.ladders import Ladder

class SnakeAndLadderUtil:

    def createBoard(board_size):
        board = []
        for i in range(board_size+1):
            board.append(i+1)
        return board

    def getStartEnd(input_string):
        space_index = input_string.find(' ')
        start = input_string[0:space_index]
        end = input_string[space_index+1:]
        return int(start), int(end)
    
    def snakeInCurrentPos(curent_pos, snakes_list):
        for i in range(len(snakes_list)):
            if curent_pos == snakes_list[i].start:
                print("snakes ****************")
                return True,  (snakes_list[i].start - snakes_list[i].end)
        return False, 0
    
    def ladderInCurrentPos(curent_pos, ladders_list):
        for i in range(len(ladders_list)):
            if curent_pos == ladders_list[i].start:
                print("ladders ****************")
                return True,  (ladders_list[i].end - ladders_list[i].start)
        return False, 0