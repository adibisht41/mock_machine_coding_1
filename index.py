from models.player import Player
from models.snakes import Snake
from models.ladders import Ladder
from util import SnakeAndLadderUtil

import random
import string


def playGame(board_size, board, snakes_list, ladders_list, players_list):

    remaining_players = len(players_list)
    i=0
    while True:
        current_player = players_list[i]
        dice_value = random.randint(0,6)

        current_position = Player.getCurrentPos(current_player)
        intial_position = current_position
        current_position = current_position + dice_value

        number_snakes_met = 0
        numner_ladders_met = 0
        while True:
            is_snake, snake_drop = SnakeAndLadderUtil.snakeInCurrentPos(current_position, snakes_list)
            is_ladder, ladder_jump = SnakeAndLadderUtil.ladderInCurrentPos(current_position, ladders_list)
            if is_snake or is_ladder:
                if is_snake:
                    current_position = current_position - snake_drop
                    number_snakes_met +=1
                elif is_ladder:
                    current_position = current_position + ladder_jump
                    numner_ladders_met+=1
            else:
                break
        if (number_snakes_met!=0) or (numner_ladders_met!=0):
            print(current_player.name+" rolled a "+ str(dice_value)+" and moved from "+ str(intial_position) +" to "+str(current_position)+"******* sankes "+ str(number_snakes_met)+" **********ladders"+str(numner_ladders_met))
        else:
            print(current_player.name+" rolled a "+ str(dice_value)+" and moved from "+ str(intial_position) +" to "+str(current_position))

        if current_position == board_size:
            print(current_player.name+ ' wins the game')
            players_list.remove(current_player)
            remaining_players -= 1
        elif current_position > board_size:
            current_position = intial_position
        Player.updateCurrentPos(current_player, current_position)
        
        if i==len(players_list)-1:
            i=0
        else:
            i+=1
        
        if remaining_players == 1:
            break
        
        
        
        



def index():
    # board_size = int(input('enter size of board'))
    board_size = 100
    board = SnakeAndLadderUtil.createBoard(board_size)

    # number_of_snakes = int(input())
    # snakes_list = []
    # for i in range(number_of_snakes):
    #     snake_input = input()
    #     snake_start, snake_end = SnakeAndLadderUtil.getStartEnd(snake_input)
    #     snake = Snake(snake_start, snake_end)
    #     snakes_list.append(snake)
    
    # number_of_ladders = int(input())
    # ladders_list = []
    # for i in range(number_of_ladders):
    #     ladder_input = input()
    #     ladder_start, ladder_end = SnakeAndLadderUtil.getStartEnd(ladder_input)
    #     ladder = Ladder(ladder_start, ladder_end)
    #     ladders_list.append(ladder)
    
    # number_of_players = int(input())
    # players_list = []
    # for i in range(number_of_players):
    #     player_name = input()
    #     player = Player(player_name)
    #     players_list.append(player)

    snakes_list_test = ['62 5', '33 6', '49 9', '88 16', '41 20', '56 53', '98 64', '93 73', '95 75']
    snakes_list = []
    for i in range(len(snakes_list_test)):
        snake_start, snake_end = SnakeAndLadderUtil.getStartEnd(snakes_list_test[i])
        snake = Snake(snake_start, snake_end)
        snakes_list.append(snake)
    
    ladders_list_test = ['2 37', '27 46', '10 32', '51 68', '61 79', '65 84', '71 91', '81 100']
    ladders_list = []
    for i in range(len(ladders_list_test)):
        snake_start, snake_end = SnakeAndLadderUtil.getStartEnd(ladders_list_test[i])
        ladder = Ladder(snake_start, snake_end)
        ladders_list.append(ladder)
    
    players = ['Gaurav', 'Sagar']
    players_list = []
    for i in range(len(players)):
        player = Player(players[i])
        players_list.append(player)


    playGame(board_size, board, snakes_list, ladders_list, players_list)
    

index()






    