import operator
from project.monopoly import Monopoly
from project.player import PLAYER_TYPE, IMPULSIVE, EXIGENT, CAUTIOUS, RANDOM

def start_game():

    _matches_to_play = 300
    _max_turns = 1000
    _num_properties = 20
    _num_players = 4
    _starting_money = 300.0
    _property_sale_range = [70.0, 150.0]
    _property_rent_range = [30.0, _property_sale_range[0]] # be careful the maximum rent value can't exceed the sale price
    total_timeout = 0
    total_turns = 0
    longest_turn = 0
    winner_type_counter = {IMPULSIVE: 0, EXIGENT: 0, CAUTIOUS: 0, RANDOM: 0}

    print('\x1b[2J\x1b[H') # clear terminal
    print('|=========================================================START=========================================================|')
    for game_num in range(_matches_to_play):
        new_game = Monopoly(num_properties=_num_properties, 
                            num_players=_num_players,
                            starting_money=_starting_money,
                            property_sale_range=_property_sale_range,
                            property_rent_range=_property_rent_range,
                            print_last_board=False)
        winner, timeout, turns = new_game.start_new_game(game_num=game_num, max_turns=_max_turns)
        total_timeout += timeout
        total_turns += turns
        longest_turn = turns if turns > longest_turn else longest_turn
        winner_type_counter[winner.type] += 1
    
    print('\nParameters: ')
    print(' _matches_to_play: ', _matches_to_play)
    print(' _max_turns: ', _max_turns)
    print(' _num_properties: ', _num_properties)
    print(' _num_players: ', _num_players)
    print(' _starting_money: ', _starting_money)
    print(' _property_sale_range: ', _property_sale_range)
    print(' _property_rent_range: ', _property_rent_range)

    print_results(winner_type_counter, total_timeout, total_turns, _matches_to_play, longest_turn)
    print('\n|==========================================================END==========================================================|\n')

def print_results(winner_type_counter, total_timeout, total_turns, _matches_played, longest_turn):

    print('\nResults:')

    # timeout matches
    print('- Matches ended by timeout: ', total_timeout)

    # matches average turns
    avg = total_turns/_matches_played  # or sum(shifts) / len(shifts)
    print('- Match turn average: ', f'{avg:.2f}')

    # longest match
    print('- Match with most turns: ', f'{longest_turn}')

    # Winner percentage by type of player
    print('- Winner percentage by type of player:')
    perc = dict()
    # calculating percentage
    for wt, v in winner_type_counter.items():
        perc[wt] = v/_matches_played*100.0
    # ordering and printing
    ordered_result = sorted(perc.items(), key=operator.itemgetter(1), reverse=True)
    for wt, v in ordered_result:
        print('  ', PLAYER_TYPE[wt], f'{v:.2f}%')
        
    # most victorious
    print('- Most victorious:')
    print('  ', PLAYER_TYPE[ordered_result[0][0]])

if __name__ == '__main__':
    start_game()