from random import random, randint, shuffle
from project.board import Board
from project.player import Player, PLAYER_TYPE, IMPULSIVE, EXIGENT, CAUTIOUS, RANDOM


class Monopoly():

    def __init__(self, num_properties, num_players, starting_money, property_sale_range, property_rent_range, print_last_board):
        self._num_properties = num_properties
        self.__new_board(num_properties, property_sale_range, property_rent_range)
        self._gamers = list()
        for n in range(num_players): # creating new players
            self._gamers.append(Player(player_id=n, type=n%4, available_money=starting_money)) # %4 because there are only 4 types of behaviors
        shuffle(self._gamers) # randomize gamers order
        self._eliminated = list()
        self._print_last_board = print_last_board
        self.winner = None
        self.timeout = False
        

    def __new_board(self, num_properties, property_sale_range, property_rent_range):
        self._board = Board(num_properties, property_sale_range, property_rent_range)._get_board()


    def start_new_game(self, game_num, max_turns=1000):
        turn = 1

        while (turn <= max_turns and not self.winner):

            # reached last turn - define the winner by greater amount of money
            if turn == max_turns:
                survivors = [x for x in self._gamers if x not in self._eliminated]
                # it already consider the tie breaker - the `max` returns the first occurrence in the gamers list order
                self.winner = max(survivors, key=lambda k: k.available_money)
                self.timeout = True
                break
            
            for current_player in self._gamers:
                # if the player was elimanited then pass to the next
                if current_player in self._eliminated:
                    continue
                # if all others players were eliminated then the game ended
                elif len(self._eliminated) == 3:
                    self.winner = current_player
                    break

                new_position = self.__calculate_new_position(current_player)
                property_on_position = self._board[new_position]

                if new_position != 0:  # If 0 then the current property is the starter position
                    property_owner = property_on_position.owner

                    # If the property has no owner
                    if not property_owner and current_player.available_money >= property_on_position.sale_price:

                        # IMPULSIVE: Buy any property
                        if current_player.type == IMPULSIVE:
                            # Buying the preporty assigning the owner of the property with the player object
                            property_on_position.owner = current_player
                            current_player.available_money -= property_on_position.sale_price # decreasing player money
                        
                        # EXIGENT: Buy any property if the rent price is greater than 50
                        elif current_player.type == EXIGENT:
                            if property_on_position.rent_price > 50.0:
                                property_on_position.owner = current_player
                                current_player.available_money -= property_on_position.sale_price
                        
                        # CAUTIONS: Buy any property if the remaining money is greater than or equal 80
                        elif current_player.type == CAUTIOUS:
                            if current_player.available_money - property_on_position.sale_price >= 80.0:
                                property_on_position.owner = current_player
                                current_player.available_money -= property_on_position.sale_price
                        
                        # RANDOM: Buy any property with 50% of probability
                        elif current_player.type == RANDOM:
                            if random() < .5:
                                property_on_position.owner = current_player
                                current_player.available_money -= property_on_position.sale_price
                    
                    # Property has an owner so just pay the rent price
                    elif property_owner and property_owner != current_player:
                        current_player.available_money -= property_on_position.rent_price
                        property_owner.available_money += property_on_position.rent_price
                else:
                    # completed a turn - earn 100
                    current_player.available_money += 100.00

                # the player spent all money - lost the game
                if current_player.available_money <= 0.0:
                    self.__eliminate_player(current_player)

            turn += 1
        
        # printing board result
        if self._print_last_board:
            self.__print_simplified_board(turn, game_num, PLAYER_TYPE[self.winner.type])

        return self.winner, self.timeout, turn

    def __eliminate_player(self, player):
        self._eliminated.append(player)
        # checking all properties and setting owner to None
        for prop in self._board:
            if prop.owner and prop.owner.player_id == player.player_id:
                prop.owner = None

    def __calculate_new_position(self, player):
        rolldice = randint(1, 6)
        new_position = player.position + rolldice

        # considering the position after a complete turn
        if new_position > self._num_properties:
            new_position -= self._num_properties
        
        player.position = new_position
        return new_position

    def __print_simplified_board(self, turn, game_num, winner):
        print('- Game number:', game_num)
        print('- Players info:')
        for gamer in self._gamers:
            print(' ', PLAYER_TYPE[gamer.type] + ': pos_' + str(gamer.position) + '/$' + str(f'{gamer.available_money:.2f}'), end=' ')
        print('\n\n- Board on turn:', turn)
        for enum, p in enumerate(self._board[1:], start=0):
            line_len = (self._num_properties)/4.0

            if (enum%line_len)+1.0 < line_len:
                if p.owner: print('  p' + str(enum+1) + '_owner:', PLAYER_TYPE[p.owner.player_id], end='  | ')
                else: print('  p' + str(enum+1) + '_owner: None', end='  | ')
            else:
                if p.owner: print('  p' + str(enum+1) + '_owner:', PLAYER_TYPE[p.owner.player_id])
                else: print('  p' + str(enum+1) + '_owner: None')
        print('\n- Winner:', winner)
        print('#############################################')